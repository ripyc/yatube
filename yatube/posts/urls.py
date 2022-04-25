from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('group/<str:slug>/', views.group_post, name="groups"),
    path("new", views.new_post, name="new_post"),
]
