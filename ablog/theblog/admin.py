from django.contrib import admin

from .models import Post
#allows blog post entries to be accessible from the admin area
admin.site.register(Post)

