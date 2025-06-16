from django.contrib import admin

# Register your models here.
from .models import Post, PostCategory, Category, Author


admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Category)
admin.site.register(Author)