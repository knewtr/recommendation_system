from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from users.forms import UserRegisterForm, UserUpdateForm
from users.models import User


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.token = secrets.token_hex(16)
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{user.token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"Перейдите по ссылке, чтобы подтвердить почту: {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[
                user.email,
            ],
        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy("users:profile")

    def get_form_class(self):
        return UserUpdateForm

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


def view_profile(request):
    user = request.user
    context = {
        "user": user,
    }
    return render(request, context=context, template_name="users/profile.html")


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "users/user_list.html"
