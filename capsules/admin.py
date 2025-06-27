from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'unlock_date', 'secret_code', 'created_at')
    readonly_fields = ('secret_code', 'created_at')
    ordering = ('-created_at',)
