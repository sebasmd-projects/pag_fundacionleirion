# Generated by Django 4.2.7 on 2024-06-23 03:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_contactmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]