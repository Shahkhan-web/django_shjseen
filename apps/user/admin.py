from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from apps.user import models, forms

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('id', 'email', 'fullname', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Personal info'), {'fields': (
            'fullname',
        )}),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'is_archived',
                'is_portal_user', 'groups', 'user_permissions',
            ),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'fullname',
                'password1',
                'password2',
                'is_portal_user'
            ),
        }),
    )
    ordering = ('-date_joined',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_archived', 'groups')
    search_fields = ('username', 'fullname', 'email')


@admin.register(models.PortalUser)
class PortalUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'fullname')
    add_form = forms.PortalUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'fullname',
                'password1',
                'password2',
            ),
        }),
    )


@admin.register(models.AdminUser)
class AdminUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'fullname')
    add_form = forms.AdminUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'fullname',
                'password1',
                'password2',
            ),
        }),
    )
