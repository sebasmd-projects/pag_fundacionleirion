import re
import uuid

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from app_core import get_app_from_path

TimeStampedModel = get_app_from_path(
    f'{settings.UTILS_PATH}.models.TimeStampedModel'
)

UserModel = get_user_model()


class SubscribeNewsletterModel(TimeStampedModel):
    user = models.ForeignKey(
        UserModel,
        verbose_name=_("usuario"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    email = models.EmailField(
        _('correo'),
        unique=True
    )

    names = models.CharField(
        _('nombres'),
        max_length=150,
        blank=True,
        null=True
    )

    cell_phone = models.CharField(
        _('celular'),
        max_length=25,
        blank=True,
        null=True
    )

    country_code = models.CharField(
        _('código de país'),
        max_length=10,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        if self.cell_phone:
            self.cell_phone = re.sub(r'\D', '', self.cell_phone)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'apps_project_page_subscribenewsletter'
        verbose_name = _('Sucribtor - Boletín')
        verbose_name_plural = _('Sucribtores - Boletín')


class NewsletterModel(TimeStampedModel):
    STATUS_CHOICES = [
        ('draft', 'Borrador'),
        ('scheduled', 'Programado'),
        ('sent', 'Enviado'),
    ]

    title = models.CharField(
        _('título'),
        max_length=255
    )

    content = models.TextField(
        _('contenido')
    )

    send_date = models.DateTimeField(
        _('fecha de envío'),
        null=True,
        blank=True
    )

    subscribers = models.ManyToManyField(
        SubscribeNewsletterModel,
        related_name='newsletters',
        verbose_name=_('suscriptores')
    )

    status = models.CharField(
        _('estado'),
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'apps_project_page_newsletter'
        verbose_name = _('Boletín')
        verbose_name_plural = _('Boletines')


class ContactModel(TimeStampedModel):
    names = models.CharField(
        _('nombres'),
        max_length=150
    )

    email = models.EmailField(
        _("correo"),
        max_length=254
    )

    title = models.CharField(
        _("título"),
        max_length=50
    )

    message = models.TextField(
        _("mensaje")
    )

    unique_id = models.UUIDField(
        default=uuid.uuid4,
        unique=True
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'apps_project_page_contact'
        verbose_name = _('Mensaje | Contáctanos')
        verbose_name_plural = _('Mensajes | Contáctanos')
