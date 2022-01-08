"""projetoPub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import inicio, form_erro_validacao, conta_nao_existe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('receitas/', include('receitas.urls')),
    path('despesas/', include('despesas.urls')),
    path('contas/', include('contas.urls')),
    path('form_erro_validacao', form_erro_validacao, name='formErroValidacao'),
    path('conta_nao_existe', conta_nao_existe, name='contaNaoExiste'),
    path('', inicio, name='inicio')
]
