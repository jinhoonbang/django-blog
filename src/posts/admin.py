from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):

    list_display = ["__unicode__", "updated", "timestamp"]

    #link of entries changes
    list_display_links = ["timestamp"]

    #allows filtering
    list_filter = ["updated", "timestamp"]

    search_fieds = ["title", "content"]

    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
