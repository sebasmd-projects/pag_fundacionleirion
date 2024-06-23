from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

admin_url = settings.ADMIN_URL

custom_apps = settings.CUSTOM_APPS

utils_path = settings.UTILS_PATH

apps_urls = [path('', include(f'{app}.urls')) for app in custom_apps]

handler400 = f'{utils_path}.views.handler400'

handler403 = f'{utils_path}.views.handler403'

handler404 = f'{utils_path}.views.handler404'

handler500 = f'{utils_path}.views.handler500'

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
        "ckeditor5/",
        include('django_ckeditor_5.urls')
    ),
    path(
        '',
        include(apps_urls)
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
