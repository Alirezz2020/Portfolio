from django.contrib import admin
from .models import Post, ContactMessage


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)



@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
