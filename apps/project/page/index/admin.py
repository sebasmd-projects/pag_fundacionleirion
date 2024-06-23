from django import forms
from django.contrib import admin
from django_countries import countries
from import_export.admin import ImportExportActionModelAdmin

from .models import NewsletterModel, SubscribeNewsletterModel, ContactModel


class SubscribeNewsletterAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country_code'].initial = 'CO'

    country_code = forms.ChoiceField(
        choices=[(code, f'{name} ({code})') for code, name in countries],
        widget=forms.Select(
            attrs={
                'id': 'id_country_code',
                'maxlength': 10,
            }
        ),
        required=False,
    )

    class Meta:
        model = SubscribeNewsletterModel
        fields = '__all__'


@admin.register(SubscribeNewsletterModel)
class SubscribeNewsletterAdmin(ImportExportActionModelAdmin):
    form = SubscribeNewsletterAdminForm


@admin.register(NewsletterModel)
class NewsletterAdmin(ImportExportActionModelAdmin):
    pass

@admin.register(ContactModel)
class ContactAdmin(ImportExportActionModelAdmin):
    readonly_fields = (
        'id',
        'created',
        'updated',
        'unique_id',
        'language'
    )