# Generated by Django 4.0.2 on 2022-02-02 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veterinaria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mascota',
            old_name='documento',
            new_name='propietario',
        ),
    ]