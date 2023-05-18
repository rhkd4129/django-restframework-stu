from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # filter_backends =[]
    search_fields = ["message"]
    list_diplay = ["pk", "messages", "author"]


# Register your models here.
