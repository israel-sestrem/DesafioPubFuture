from django.urls import path
from .views import listar_contas, cadastrar_contas, editar_contas, deletar_contas, conta_cadastrada

urlpatterns = [
    path('cadastrar_contas', cadastrar_contas, name='cadastrarContas'),
    path('editar_contas/<int:id>', editar_contas, name='editarContas'),
    path('deletar_contas/<int:id>', deletar_contas, name='deletarContas'),
    path('conta_cadastrada', conta_cadastrada, name='contaCadastrada'),
    path('', listar_contas, name='listarContas')
]