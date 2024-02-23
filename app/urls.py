from django.urls import path
from . views import *
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path("", index, name="index"),
    path("login/", login_user, name="login"),
    path("register/", register_user, name="register"),
    path("verify-username", csrf_exempt(verify_username), name="verify-username"),
    path("verify-email", csrf_exempt(verify_email), name="verify-email"),
    path("success/", success, name="success"),
    path("logout/", logout_user, name="logout"),
]
