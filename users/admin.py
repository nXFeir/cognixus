from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from users.models import User
from django.contrib import admin


class CustomUserAdmin(UserAdmin):
    list_display = ('uuid', ) + UserAdmin.list_display 
    search_fields = ('uuid', ) + UserAdmin.search_fields

admin.site.register(User, CustomUserAdmin)