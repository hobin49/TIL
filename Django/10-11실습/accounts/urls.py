from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.temp, name="temp"),
    path("accounts/", views.index, name="index"),
    path("accounts/signup/", views.signup, name="signup"),
    path("accounts/<int:pk>/", views.detail, name="detail"),
]
