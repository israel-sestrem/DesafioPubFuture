from django.shortcuts import render
from contas.models import Conta

def inicio(request):
    return render(request, 'principal/index.html')

def form_erro_validacao(request):
    return render(request, 'form_erros/form_erro_validacao.html')

def conta_nao_existe(request):
    contas = Conta.objects.all().order_by('id')
    totalContas = Conta.objects.all().count()
    dados = {
        'contas' : contas,
        'totalContas' : totalContas
    }
    return render(request, 'form_erros/conta_nao_existe.html', dados)