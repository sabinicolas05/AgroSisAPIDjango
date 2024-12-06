# Generated by Django 5.1.2 on 2024-12-03 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('IoT', '0001_initial'),
        ('Trazabilidad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='fk_bancal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Trazabilidad.bancal'),
        ),
        migrations.AddField(
            model_name='sensor',
            name='fk_configuracion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='IoT.configuracion'),
        ),
        migrations.AddField(
            model_name='sensor',
            name='fk_tipo_sensor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='IoT.tipo_sensor'),
        ),
    ]