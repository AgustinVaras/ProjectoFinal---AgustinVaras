from django.urls import path
from core.views import inicio, login_form

urlpatterns = [
    path("", inicio, name="index.html"),
    path("login", login_form, name="login")
]
