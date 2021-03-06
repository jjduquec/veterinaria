# Generated by Django 4.0.2 on 2022-02-02 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veterinaria', '0005_alter_producto_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroClinico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=10)),
                ('detalle', models.CharField(max_length=1000)),
                ('id_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinaria.mascota')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinaria.producto')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinaria.usuario')),
            ],
        ),
    ]
