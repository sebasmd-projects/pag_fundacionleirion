# Generated by Django 4.2.7 on 2024-06-23 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usermodel_country_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usermodel',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='country_code',
            field=models.CharField(blank=True, default='CO', max_length=10, null=True, verbose_name='código de país'),
        ),
    ]
