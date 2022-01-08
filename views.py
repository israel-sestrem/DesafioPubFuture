from django.shortcuts import render, redirect
from .models import Conta
from .forms import FormConta

# Create your views here.

def listar_contas(request):
    contas = Conta.objects.all().order_by('id')
    totalContas = Conta.objects.all().count()
    totalSaldo = 0
    for conta in contas:
        totalSaldo += int(conta.saldo)
    dados = {
        'contas' : contas,
        'totalContas' : totalContas,
        'totalSaldo' : totalSaldo
    }
    return render(request, 'contas/inicio.html', dados)

def cadastrar_contas(request):
    if ( request.method == 'POST' ):
        form = FormConta(request.POST)
        if ( form.is_valid() ):
            form.save()
            return redirect('listarContas')
        else:
            try:
                conta = Conta.objects.get(conta=form['conta'].value())
                return redirect('contaCadastrada')
            except:
                return redirect('formErroValidacao')
    else:
        return render(request, 'contas/cadastrar_contas.html')

def editar_contas(request, id):
    conta = Conta.objects.get(id=id)
    if ( request.method == 'POST' ):
        form = FormConta(request.POST, instance=conta)
        if ( form.is_valid() ):
            form.save()
            return redirect('listarContas')
        else:
            return redirect('formErroValidacao')
    else:
        return render(request, 'contas/editar_contas.html', {'conta' : conta})

def deletar_contas(request, id):
    conta = Conta.objects.get(id=id)
    if ( request.method == 'POST' ):
        conta.delete()
        return redirect('listarContas')
    else:
        return render(request, 'contas/deletar_contas.html', {'conta' : conta})

def conta_cadastrada(request):
    return render(request, 'form_erros/conta_cadastrada.html')