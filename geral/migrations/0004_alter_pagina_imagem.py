# Generated by Django 4.1 on 2022-09-09 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geral', '0003_alter_pagina_imagem_alter_pagina_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagina',
            name='imagem',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
