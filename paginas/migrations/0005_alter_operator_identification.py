# Generated by Django 3.2.8 on 2021-12-13 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0004_alter_client_identification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='identification',
            field=models.CharField(help_text='Informe o CPF do operador', max_length=11),
        ),
    ]
