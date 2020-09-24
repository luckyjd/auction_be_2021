from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserCustomAdmin(admin.ModelAdmin):
    model = User
    fieldsets = (
        (('User'), {'fields': ('username', 'email', 'password')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff')}),
    )

    list_filter = ['is_staff', 'size']  # bo loc
    search_fields = ['username', 'email']  # bo search


admin.site.register(User, UserCustomAdmin)
