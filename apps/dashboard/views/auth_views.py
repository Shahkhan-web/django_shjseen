from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url

from apps.dashboard.forms.auth_forms import LoginForm


class DashboardLoginView(LoginView):
    form_class = LoginForm

    template_name = 'auth/dashboard_login.html'
    login_redirect_url = 'list_all_participant'

    def form_valid(self, form):
        user = form.get_user()
        # 1. if user is archived
        if user.is_archived:
            form.add_error(None, "User is archived")
            return self.render_to_response(self.get_context_data(form=form))

        # 1. if user is portal user
        if not user.is_portal_user and not user.is_superuser:
            form.add_error(None, "User is not authorized")
            return self.render_to_response(self.get_context_data(form=form))

        login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url(self.login_redirect_url)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(resolve_url(self.login_redirect_url))
        return self.render_to_response(self.get_context_data())
