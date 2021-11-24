# Generated by Django 3.2.8 on 2021-11-24 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0002_auto_20211124_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Digite o nome completo do operador', max_length=50)),
                ('identification', models.DateField(help_text='Informe o CPF do operador')),
                ('area', models.CharField(help_text='Informe a área do operador', max_length=100)),
                ('department', models.CharField(help_text='Informe o departamento do operador', max_length=100)),
                ('rank', models.CharField(help_text='Informe o cargo do operador', max_length=100)),
                ('payment', models.CharField(help_text='Informe o salário do operador', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Digite o nome completo do operador', max_length=50)),
                ('stage', models.DateField(help_text='Informe o CPF do operador')),
                ('level', models.CharField(help_text='Informe a área do operador', max_length=100)),
                ('price', models.CharField(help_text='Informe o departamento do operador', max_length=100)),
            ],
        ),
    ]
