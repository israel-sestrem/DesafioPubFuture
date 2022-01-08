from django.forms import ModelForm
from .models import Receita

class FormReceita(ModelForm):
    class Meta:
        model = Receita
        fields = '__all__'