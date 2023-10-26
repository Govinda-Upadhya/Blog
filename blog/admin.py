from django.contrib import admin
from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={
        "slug":("title",)
    }
    list_display=("title", "author","date",)
    list_filter=("author",)

class AuthorAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name",)
class CommentAdmin(admin.ModelAdmin):
    list_display=("user_name","email")

admin.site.register(Post,PostAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Comments,CommentAdmin)



