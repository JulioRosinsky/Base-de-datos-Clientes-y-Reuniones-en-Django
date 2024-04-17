# Generated by Django 4.2.6 on 2024-03-25 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_bd', '0006_rename_sociedades_familia_entidades'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familia',
            name='entidades',
        ),
        migrations.AlterField(
            model_name='familia',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.DeleteModel(
            name='Sociedad',
        ),
    ]
