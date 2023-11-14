from django.urls import path, include

urlpatterns = [
    path(
        '',
        include('apps.dashboard.urls.auth_urls')
    ),
    path(
        'participant/',
        include('apps.dashboard.urls.participant_urls')
    )

]
