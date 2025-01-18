from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
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
        context["users"] = self.get_users_data()
        return context

    def get_users_data(self) -> list[dict]:
        users = User.objects.all()
        users_data = []
        for user in users:
            users_data.append(
                {
                    "name": user.username,
                    "link": f"/chat/{self.request.user.username}/{user.username}/",
                }
            )
        return users_data


class SignOutView(LogoutView):
    template_name = "logout.html"


class RoomView(LoginRequiredMixin, TemplateView):
    template_name = "room.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["first_user"] = kwargs.get("first")
        context["second_user"] = kwargs.get("second")
        return context
