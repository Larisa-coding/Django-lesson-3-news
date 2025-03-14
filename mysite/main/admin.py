from django.contrib import admin
from .models import NewsPost

@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')  # Отображаемые поля
    list_filter = ('pub_date', 'author')            # Фильтры
    search_fields = ('title', 'text')               # Поиск