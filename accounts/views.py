from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm


class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "accounts/login.html"

    def get_success_url(self):
        return reverse_lazy("index")


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = settings.LOGIN_URL
    permission_denied_message = "이미 가입한 사용자 입니다!"


login = UserLoginView.as_view()
logout = LogoutView.as_view(next_page=settings.LOGIN_URL)
signup = SignUpView.as_view()
