from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

from channel.forms import LogoutForm


class SignInView(LoginView):
    template_name = "signin.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["logout_form"] = LogoutForm()
        return context


class SignOutView(LogoutView):
    template_name = "logout.html"
