# Generated by Django 4.2.6 on 2024-02-21 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_de_nacimiento', models.DateField(default='1432-01-01')),
                ('direcion', models.CharField(max_length=100)),
                ('activo', models.BooleanField(default=False)),
                ('relevancia', models.CharField(choices=[('Altísima', 'Altísima'), ('Alta', 'Alta'), ('Media', 'Media'), ('Baja', 'Baja')], max_length=20, null=True)),
                ('ejecutivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientes_ejecutivos', to=settings.AUTH_USER_MODEL)),
                ('familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientes_familia', to='landing_bd.familia')),
            ],
        ),
    ]