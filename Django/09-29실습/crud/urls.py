from django.urls import path
from . import views

app_name = "crud"

urlpatterns = [
    path("create", views.create, name="create"),
    path("read/", views.read, name="read"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("update/<int:pk_>", views.update, name="update"),
]
