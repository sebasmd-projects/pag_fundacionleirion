from django.urls import path

from .views import SubscribeNewsletterFormView, IndexTemplateView

app_name = "index"

urlpatterns = [
    path(
        '',
        IndexTemplateView.as_view(),
        name='home'
    ),
    path(
        'suscripcion/',
        SubscribeNewsletterFormView.as_view(),
        name='subscribe_newsletter'
    ),
]
