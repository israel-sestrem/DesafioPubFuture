from django.urls import path
from .views import listar_receitas, cadastrar_receitas, editar_receitas, deletar_receitas

urlpatterns = [
    path('cadastrar_receitas', cadastrar_receitas, name='cadastrarReceitas'),
    path('editar_receitas/<int:id>', editar_receitas, name='editarReceitas'),
    path('deletar_receitas/<int:id>', deletar_receitas, name='deletarReceitas'),
    path('', listar_receitas, name='listarReceitas')
]