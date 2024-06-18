from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views as auth_views

admin_url = settings.ADMIN_URL
custom_apps = settings.CUSTOM_APPS

apps_urls = [path('', include(f'{app}.urls')) for app in custom_apps]

urlpatterns = [
    path(admin_url, admin.site.urls),
    re_path(
        r"^sitemap.xml",
        sitemap,
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path(
        "accounts/login/",
        auth_views.LoginView.as_view()
    ),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view()
    ),
    path(
        '',
        include(apps_urls)
    )
]
