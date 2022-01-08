from django.forms import ModelForm
from .models import Conta

class FormConta(ModelForm):
    class Meta:
        model = Conta
        fields = '__all__'