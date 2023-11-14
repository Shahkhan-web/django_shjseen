from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django_filters.views import FilterView

from rest_framework import generics

from apps.core.decorators import admin_or_portal_user_required
from apps.dashboard import filtersets, usecases
from apps.participant.models import Participant


@method_decorator(admin_or_portal_user_required(login_url='dashboard_login'), name='dispatch')
class ListAllParticipantView(FilterView, ListView):
    template_name = 'participant/list_all_participant.html'
    filterset_class = filtersets.ParticipantFilter
    paginate_by = 50

    def get_queryset(self):
        return Participant.objects.order_by('-created')


class ExportAllParticipantView(generics.ListAPIView):
    pagination_class = None
    filterset_class = filtersets.ParticipantFilter

    def get_queryset(self):
        return Participant.objects.unarchived()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        return usecases.ExportAllParticipantUseCase(queryset=queryset).execute()
