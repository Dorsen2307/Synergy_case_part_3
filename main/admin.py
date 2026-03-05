from django.contrib import admin
from .models import UserName

@admin.register(UserName)
class UserNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)
    ordering = ('-id',)