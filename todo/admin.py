from django.contrib import admin
from .models import TodoItem

class TodoItemAdmin(admin.ModelAdmin):
    model = TodoItem
    list_display  = ('uuid', 'user', 'title', 'start_time', 'is_completed', 'created_at', 'updated_at')
    ordering = ('user', 'created_at')
    readonly_fields = ('uuid', 'created_at', 'updated_at')
    fields = ('uuid', 'user', 'title', 'start_time', 'is_completed', 'created_at', 'updated_at')

admin.site.register(TodoItem, TodoItemAdmin)
    