# Generated by Django 4.2.6 on 2024-02-26 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing_bd', '0002_alter_cliente_fecha_de_nacimiento_reuniones'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reuniones',
            old_name='arvhivo',
            new_name='archivo',
        ),
    ]
