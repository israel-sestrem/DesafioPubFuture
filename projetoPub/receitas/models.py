from django.db import models
from django.db.models.fields import CharField, DateField, DecimalField, IntegerField

# Create your models here.

class Receita(models.Model):
    valor = IntegerField()
    data_recebimento = DateField()
    data_recebimento_esperado = DateField()
    descricao = CharField(max_length=100)
    conta = IntegerField()
    tipo_receita = CharField(max_length=30)

    class Meta:
        db_table = 'receitas'