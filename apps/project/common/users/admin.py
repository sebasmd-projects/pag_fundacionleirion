from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportActionModelAdmin

from .models import UserModel


@admin.register(UserModel)
class UserModelAdmin(UserAdmin, ImportExportActionModelAdmin):
    search_fields = (
        'id',
        'username',
        'email',
        'cell_phone',
        'first_name',
        'last_name',
    )

    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
    )

    list_display = (
        'get_full_name',
        'username',
        'email',
        'cell_phone',
        'is_staff',
        'is_active'
    )

    list_display_links = (
        'get_full_name',
        'username',
        'email',
    )

    ordering = (
        'default_order',
        'created',
        'last_name',
        'first_name',
        'email',
        'username',
    )

    readonly_fields = (
        'created',
        'updated',
        'last_login',
        'get_age'
    )

    fieldsets = (
        (
            _('Información de usuario'), {
                'fields': (
                    'username',
                    'password'
                )
            }
        ),
        (
            _('Información personal'), {
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'cell_phone',
                    'birthday',
                    'get_age',
                )
            }
        ),
        (
            _('Permisos'), {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions'
                )
            }
        ),
        (
            _('Fechas'), {
                'fields': (
                    'last_login',
                    'created',
                    'updated'
                )
            }
        ),
        (
            _('Orden por defecto'), {
                'fields': (
                    'default_order',
                )
            }
        )
    )

    def get_age(self, obj):
        return obj.get_age()

    def get_full_name(self, obj):
        return obj.get_full_name()

    get_full_name.short_description = _('Nombres completos')

    get_age.short_description = _('Edad')
