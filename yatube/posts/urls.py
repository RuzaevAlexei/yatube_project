from django.urls.resolvers import URLPattern
from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('group/<slug:slug>/', views.group_posts, name='group_posts'),  # Страницы постов по группам
] 