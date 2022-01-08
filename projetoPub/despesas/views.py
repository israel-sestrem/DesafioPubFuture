from django.shortcuts import render, redirect
from .models import Despesa
from .forms import FormDespesa
from contas.models import Conta

# Create your views here.

def listar_despesas(request):
    despesas = Despesa.objects.all().order_by('data_pagamento')
    totalDespesas = Despesa.objects.all().count()
    dados = {
        'despesas' : despesas,
        'totalDespesas' : totalDespesas
    }
    return render(request, 'despesas/inicio.html', dados)

def cadastrar_despesas(request):
    if ( request.method == 'POST' ):
        form = FormDespesa(request.POST)
        if ( form.is_valid() ):
            numeroConta = int(form['conta'].value())
            contas = Conta.objects.all()
            for conta in contas:
                if ( conta.conta == numeroConta ):
                    form.save()
                    return redirect('listarDespesas')
            return redirect('contaNaoExiste')
        else:
            return redirect('formErroValidacao')
    else:
        return render(request, 'despesas/cadastrar_despesas.html')

def editar_despesas(request, id):
    despesa = Despesa.objects.get(id=id)
    if ( request.method == 'POST' ):
        form = FormDespesa(request.POST, instance=despesa)
        if ( form.is_valid() ):
            numeroConta = int(form['conta'].value())
            contas = Conta.objects.all()
            for conta in contas:
                if ( conta.conta == numeroConta ):
                    form.save()
                    return redirect('listarDespesas')
            return redirect('contaNaoExiste')
        else:
            return redirect('formErroValidacao')
    else:
        return render(request, 'despesas/editar_despesas.html', {'despesa' : despesa})

def deletar_despesas(request, id):
    despesa = Despesa.objects.get(id=id)
    if ( request.method == 'POST' ):
        despesa.delete()
        return redirect('listarDespesas')
    else:
        return render(request, 'despesas/deletar_despesas.html', {'despesa' : despesa})