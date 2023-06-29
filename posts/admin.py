from django.contrib import admin
from.models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'create_date',)
    search_fields = ('title', 'text',)
    list_filter = ('id',)

@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name','create_date',)
    readonly_fields = ('create_date',)
    search_fields = ('name','text',)
    list_filter= ('create_date',)