from django.contrib import admin
from .models import TodoModel, CategoryModel

admin.site.register(CategoryModel)

@admin.register(TodoModel)
class TodoModelAdmin(admin.ModelAdmin):
    list_display = ['task_name', 'created_at']
    list_display_links = ['task_name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['task_name', 'created_at']