from django.contrib import admin
from .models import arrr

@admin.register(arrr)
class ArrrAdmin(admin.ModelAdmin):
    list_display = ('title', 'token', 'key')
    search_fields = ('title', 'token')
    readonly_fields = ('key',)