# Generated by Django 4.0.8 on 2023-01-14 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quality_control', '0003_regime'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Regime',
            new_name='Regimes',
        ),
        migrations.AlterModelTable(
            name='regimes',
            table='AV_REGIMES',
        ),
    ]