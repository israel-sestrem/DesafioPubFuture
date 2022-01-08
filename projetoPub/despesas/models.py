from django.db import models
from django.db.models.fields import CharField, DateField, DecimalField, IntegerField

# Create your models here.

class Despesa(models.Model):
    valor = IntegerField()
    data_pagamento = DateField()
    data_pagamento_esperado = DateField()
    tipo_despesa = CharField(max_length=30)
    conta = IntegerField()

    class Meta:
        db_table = 'despesas'