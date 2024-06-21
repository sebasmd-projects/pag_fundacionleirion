from django import forms
from django_countries import countries

from .models import SubscribeNewsletterModel


class SubscribeNewsletterForm(forms.ModelForm):
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

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'id': 'id_email',
                'maxlength': 254,
                'placeholder': 'email@correo.com'
            }
        ),
        required=True,
    )

    names = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'id_names',
                'maxlength': 150,
                'placeholder': 'Nombres'
            }
        ),
        required=False,
    )

    cell_phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'id_cell_phone',
                'maxlength': 25,
                'placeholder': '300 000 00 00'
            }
        ),
        required=False,
    )

    class Meta:
        model = SubscribeNewsletterModel
        fields = ['email', 'names', 'cell_phone', 'country_code']
