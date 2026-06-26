from django.contrib import admin
from .models import Book, Category, ISBN

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'rate', 'views')
    admin.site.register(Category)