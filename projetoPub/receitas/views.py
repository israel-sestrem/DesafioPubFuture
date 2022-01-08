from django.shortcuts import redirect, render
from .models import Receita
from .forms import FormReceita
from contas.models import Conta

# Create your views here.

def listar_receitas(request):
    receitas = Receita.objects.all().order_by('data_recebimento')
    totalReceitas = Receita.objects.all().count()
    dados = {
        'receitas' : receitas,
        'totalReceitas' : totalReceitas
    }
    return render(request, 'receitas/inicio.html', dados)

def cadastrar_receitas(request):
    if ( request.method == 'POST' ):
        form = FormReceita(request.POST)
        if ( form.is_valid() ):
            numeroConta = int(form['conta'].value())
            contas = Conta.objects.all()
            for conta in contas:
                if ( conta.conta == numeroConta ):
                    form.save()
                    return redirect('listarReceitas')
            return redirect('contaNaoExiste')
        else:
            return redirect('formErroValidacao')
    else:
        return render(request, 'receitas/cadastrar_receitas.html')

def editar_receitas(request, id):
    receita = Receita.objects.get(id=id)
    if ( request.method == 'POST' ):
        form = FormReceita(request.POST, instance=receita)
        if ( form.is_valid() ):
            numeroConta = int(form['conta'].value())
            contas = Conta.objects.all()
            for conta in contas:
                if ( conta.conta == numeroConta ):
                    form.save()
                    return redirect('listarReceitas')
            return redirect('contaNaoExiste')
        else:
            return redirect('formErroValidacao')
    else:
        return render(request, 'receitas/editar_receitas.html', {'receita' : receita})

def deletar_receitas(request, id):
    receita = Receita.objects.get(id=id)
    if ( request.method == 'POST' ):
        receita.delete()
        return redirect('listarReceitas')
    else:
        return render(request, 'receitas/deletar_receitas.html', {'receita' : receita})