from django.shortcuts import render
from .models import NewsPost

def home(request):
    """Главная страница"""
    return render(request, 'main/layoute.html')

def news_home(request):
    """Страница со всеми новостями"""
    news = NewsPost.objects.all().order_by('-pub_date')  # Сортировка от новых к старым
    return render(request, 'main/news.html', {'news': news})