from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "accounts/login.html"

    def get_success_url(self):
        return reverse_lazy("index")


login = UserLoginView.as_view()
logout = LogoutView.as_view(next_page="login")
