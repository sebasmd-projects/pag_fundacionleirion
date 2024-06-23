# Generated by Django 4.2.7 on 2024-06-23 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribenewslettermodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='usuario'),
        ),
        migrations.AddField(
            model_name='newslettermodel',
            name='subscribers',
            field=models.ManyToManyField(related_name='newsletters', to='index.subscribenewslettermodel', verbose_name='suscriptores'),
        ),
        migrations.AddField(
            model_name='newslettermodel',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='index.newslettertemplate', verbose_name='plantilla'),
        ),
    ]
