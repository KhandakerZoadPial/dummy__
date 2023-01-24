# Generated by Django 4.0.8 on 2023-01-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality_control', '0004_rename_regime_regimes_alter_regimes_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regimes',
            name='question',
        ),
        migrations.AddField(
            model_name='regimes',
            name='question',
            field=models.ManyToManyField(blank=True, help_text='A regime can have multiple questions', to='quality_control.questions'),
        ),
    ]