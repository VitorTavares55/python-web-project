# Generated by Django 4.0.2 on 2022-02-11 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='cpf',
            new_name='identification',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='nome_completo',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='telefone',
            new_name='phone',
        ),
    ]
