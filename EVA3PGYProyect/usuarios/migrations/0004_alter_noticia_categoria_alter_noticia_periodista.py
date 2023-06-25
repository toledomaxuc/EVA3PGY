# Generated by Django 4.1.2 on 2023-06-24 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_noticia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='categoria',
            field=models.CharField(choices=[('POPULAR', 'POPULAR'), ('POLITICA', 'POLITICA'), ('DEPORTE', 'DEPORTE')], max_length=50),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='periodista',
            field=models.CharField(choices=[('Maria Plaza', 'Maria Plaza'), ('Isabel Caro', 'Isabel Caro'), ('Cesar Vasquez', 'Cesar Vasquez')], max_length=100),
        ),
    ]
