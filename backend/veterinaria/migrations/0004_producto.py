# Generated by Django 4.0.2 on 2022-02-02 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veterinaria', '0003_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
