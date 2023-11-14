from django.urls import path

from apps.dashboard.views import participant_views

urlpatterns = [
    path(
        'all',
        participant_views.ListAllParticipantView.as_view(),
        name='list_all_participant'
    ),
    path(
        'export',
        participant_views.ExportAllParticipantView.as_view(),
        name='export_all_participant'
    ),
    # path(
    #     '<int:pos_id>/export_single_data',
    #     pos_data_views.ExportSinglePosDataView.as_view(),
    #     name = 'export_single_data'
    # ),
]
