from django.contrib.auth.views import LogoutView
from django.urls import path

from apps.dashboard.views import auth_views

urlpatterns = [
    path(
        'login',
        auth_views.DashboardLoginView.as_view(),
        name='dashboard_login'
    ),
    path(
        'logout',
        LogoutView.as_view(),
        name='dashboard_logout'
    ),
]
