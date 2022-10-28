from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("<int:user_pk>/", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]
