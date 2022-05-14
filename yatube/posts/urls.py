from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('404', views.page_not_found, name='404'),
    path('500', views.server_error, name='500'),
    path('group/<str:slug>/', views.group_post, name='groups'),
    path('new', views.new_post, name='new_post'),
    path('<str:username>/', views.profile, name='profile'),  # Профайл пользователя
    path('<str:username>/<int:post_id>/', views.post_view, name='post'),  # Просмотр записи
    path('<str:username>/<int:post_id>/edit/', views.post_edit, name='post_edit'),  # Редактирование записи
]
