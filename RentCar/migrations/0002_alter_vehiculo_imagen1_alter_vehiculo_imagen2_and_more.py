# Generated by Django 4.0.4 on 2022-06-20 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RentCar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='imagen1',
            field=models.ImageField(null=True, upload_to='vehiculos'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='imagen2',
            field=models.ImageField(null=True, upload_to='vehiculos'),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='imagen3',
            field=models.ImageField(null=True, upload_to='vehiculos'),
        ),
    ]
