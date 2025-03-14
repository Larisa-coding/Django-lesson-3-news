from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),          # Главная страница
    path('news/', views.news_home, name='news_home'),  # Страница новостей
]