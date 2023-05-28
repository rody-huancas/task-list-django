from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("registro/", views.register_user, name="registro"),
    path("logout/", views.logout, name="logout"),
]
