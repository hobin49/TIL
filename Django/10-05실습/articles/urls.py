from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # 생성
    path("create/", views.create, name="create"),
    # 삭제
    path("<int:pk>/delete", views.delete, name="delete"),
    # 상세보기
    path("<int:pk>/detail", views.detail, name="detail"),
    # 업데이트하기
    path("<int:pk>/update", views.update, name="update"),
]
