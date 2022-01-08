from django.db import models
from django.db.models.fields import CharField, DateField, DecimalField

# Create your models here.

class Conta(models.Model):
    conta = DecimalField(max_digits=6, decimal_places=0, unique=True)
    saldo = CharField(max_length=15)
    tipo_conta = CharField(max_length=30)
    instituicao_financeira = CharField(max_length=50)

    class Meta:
        db_table = 'contas'