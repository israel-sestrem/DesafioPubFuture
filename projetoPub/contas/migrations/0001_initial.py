# Generated by Django 3.2.5 on 2022-01-08 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conta', models.DecimalField(decimal_places=0, max_digits=6, unique=True)),
                ('saldo', models.CharField(max_length=15)),
                ('tipo_conta', models.CharField(max_length=30)),
                ('instituicao_financeira', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'contas',
            },
        ),
    ]
