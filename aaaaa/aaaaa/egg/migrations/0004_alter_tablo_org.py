# Generated by Django 5.1.6 on 2025-02-22 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egg', '0003_rename_id_intepretation_tablo_id_interpretation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablo',
            name='org',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Организацияz'),
        ),
    ]
