"""
Django admin customizations
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models


# @admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    """
    define the admin pages for users
    """
    ordering = ['id']
    list_display = ['email', 'name']


admin.site.register(models.User, UserAdmin)
