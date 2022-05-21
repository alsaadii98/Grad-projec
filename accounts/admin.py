from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUser
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'phone', 'is_staff', ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone', )}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
