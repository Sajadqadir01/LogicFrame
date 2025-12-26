from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models

@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('last_name', 'email', 'currency', 'last_login', 'is_active')
    list_filter = ('currency', )
    list_editable = ('is_active', )
