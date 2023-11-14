import django_filters
from django.db.models import Q
from django_filters import rest_framework as filters


class ParticipantFilter(django_filters.FilterSet):
    date = filters.DateFromToRangeFilter(
        field_name='created__date',
        label='date',
    )

    search = django_filters.CharFilter(method='search_filter')

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(organization_name__icontains=value) |
            Q(category_name__icontains=value) |
            Q(contact_person_name__icontains=value)
        )
