# Generated by Django 4.2.7 on 2024-06-23 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='country_code',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='código de país'),
        ),
    ]
