# Generated by Django 4.0.2 on 2022-02-03 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veterinaria', '0006_registroclinico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=9)),
                ('total', models.IntegerField()),
                ('id_propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinaria.propietario')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinaria.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.IntegerField()),
                ('id_factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinaria.factura')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinaria.producto')),
            ],
        ),
    ]
