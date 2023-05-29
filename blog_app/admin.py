from django.contrib import admin
from .models import Post, Comment, Tag, Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Profile)
