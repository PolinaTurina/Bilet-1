from django.contrib import admin
from.models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'create_date',)
    search_fields = ('title', 'text',)
    list_filter = ('id',)
