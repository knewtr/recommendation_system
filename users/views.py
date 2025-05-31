from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.views import LogoutView as AuthLogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from connections.models import Connection
from users.forms import UserLoginForm, UserRegisterForm, UserUpdateForm
from users.models import User


class RegisterView(LoginRequiredMixin, CreateView):
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Вы успешно зарегистрировались!")
        return response


class LoginView(AuthLoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm
    success_url = reverse_lazy("books:home")

    def form_valid(self, form):
        from django.contrib.auth import login

        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


class LogoutView(AuthLogoutView):
    next_page = reverse_lazy("users:login")

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Возвращайтесь!")
        return super().dispatch(request, *args, **kwargs)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy("users:profile")

    def get_form_class(self):
        return UserUpdateForm

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "users/user_list.html"
    paginate_by = 10


class ProfileView(DetailView):
    model = User
    template_name = "users/profile.html"
    context_object_name = "user_profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rating"] = Connection.objetcs.filter(user=self.object).select_related(
            "book"
        )
        return context
