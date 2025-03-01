# Generated by Django 5.1.6 on 2025-03-01 00:54

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aappii_d', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='arrr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255, unique=True)),
                ('key', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='token',
        ),
    ]
