from django.db import models
from django.db.models.fields import CharField, DateField, DecimalField, IntegerField

# Create your models here.

class Conta(models.Model):
    conta = IntegerField(unique=True)
    saldo = IntegerField()
    tipo_conta = CharField(max_length=30)
    instituicao_financeira = CharField(max_length=50)

    class Meta:
        db_table = 'contas'