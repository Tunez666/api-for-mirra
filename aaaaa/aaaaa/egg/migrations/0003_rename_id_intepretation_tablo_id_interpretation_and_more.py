# Generated by Django 5.1.6 on 2025-02-22 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egg', '0002_alter_tablo_abbreviation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tablo',
            old_name='id_intepretation',
            new_name='id_interpretation',
        ),
        migrations.RenameField(
            model_name='tablo',
            old_name='oid_intepretation',
            new_name='oid_interpretation',
        ),
        migrations.RemoveField(
            model_name='tablo',
            name='abbreviation',
        ),
        migrations.RemoveField(
            model_name='tablo',
            name='name_eng',
        ),
        migrations.AlterField(
            model_name='tablo',
            name='oid_parameter',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='OID справочника с параметрами шкалы'),
        ),
        migrations.AlterField(
            model_name='tablo',
            name='point_scale',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Признак балльной шкалы'),
        ),
        migrations.AlterField(
            model_name='tablo',
            name='valid',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Валидация'),
        ),
        migrations.AlterField(
            model_name='tablo',
            name='valid_author',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Названия и авторы'),
        ),
        migrations.AlterField(
            model_name='tablo',
            name='valid_doi',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Идентификатор публикации'),
        ),
    ]
