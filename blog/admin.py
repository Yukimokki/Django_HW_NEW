from django.contrib import admin
from blog.models import Blog_Entry


@admin.register(Blog_Entry)
class Blog_EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "preview", "is_published",)
    list_filter = ("is_published",)
    search_fields = ("title", "creation_date")