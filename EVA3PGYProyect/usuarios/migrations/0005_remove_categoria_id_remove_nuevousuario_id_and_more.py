# Generated by Django 4.1.2 on 2023-06-24 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0004_formcategoria_remove_categoria_nombre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='id',
        ),
        migrations.RemoveField(
            model_name='nuevousuario',
            name='id',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='id',
        ),
        migrations.AlterField(
            model_name='categoria',
            name='idCategoria',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='nuevousuario',
            name='idUsuario',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='idPublicacion',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='idUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='imagen',
            field=models.ImageField(upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='titulo',
            field=models.CharField(max_length=255),
        ),
    ]
