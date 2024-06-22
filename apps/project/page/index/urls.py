from django.urls import path

from .views import SubscribeNewsletterFormView, IndexTemplateView, ContactFormView

app_name = "index"

urlpatterns = [
    path(
        '',
        IndexTemplateView.as_view(),
        name='home'
    ),
    path(
        'boletin/suscripcion/',
        SubscribeNewsletterFormView.as_view(),
        name='subscribe_newsletter'
    ),
    path(
        'contact/',
        ContactFormView.as_view(),
        name='contact'
    )
]
