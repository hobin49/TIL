# Register your models here.
# list_display = ('title', 'created_at', 'updated_at')
from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")


# admin.site.register(Article)
admin.site.register(Article, ArticleAdmin)
