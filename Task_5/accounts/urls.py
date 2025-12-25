from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import register, my_profile

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="../../accounts/templates/accounts/login.html"), name="login"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="../../accounts/templates/accounts/logout.html"),
        name="logout"
    ),
    path("profile/", my_profile, name="my_profile"),

]