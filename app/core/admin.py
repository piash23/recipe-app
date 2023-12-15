"""
Django admin customizations
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext as _  # future proofing


# @admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    """
    define the admin pages for users
    """
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        (_('Personal Info'), {
            'fields': ('name',)
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        (_('Important dates'), {
            'fields': ('last_login',)
        })
    )
    readonly_fields = ('last_login',)


admin.site.register(models.User, UserAdmin)
