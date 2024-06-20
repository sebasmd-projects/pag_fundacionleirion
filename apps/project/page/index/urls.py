from django.urls import include, path

from .views import IndexTemplateView

urlpatterns = [
    path(
        '',
        IndexTemplateView.as_view(),
        name='index'
    )
]