from django.contrib import admin

from apps.core.admin import BaseModelAdmin
from apps.participant import models


@admin.register(models.Category)
class CategoryAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'name',
    )
    search_fields = BaseModelAdmin.search_fields + (
        'name',
    )


@admin.register(models.Participant)
class ParticipantAdmin(BaseModelAdmin):
    list_display = BaseModelAdmin.list_display + (
        'organization_name',
    )
    search_fields = BaseModelAdmin.search_fields + (
        'organization_name',
    )
    list_filter = BaseModelAdmin.list_filter + (
        'category_name',
        'organization_type',
        'organization_location',
        'is_first_time',
    )
