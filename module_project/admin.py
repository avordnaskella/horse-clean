from django.contrib import admin

# Register your models here.
from .models import Category, Discipline

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'difficulty', 'is_olympic', 'created_at')
    list_filter = ('category', 'difficulty', 'is_olympic')
    search_fields = ('name', 'description')