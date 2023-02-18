from django.contrib import admin
from .models import Post

# After creating our model Post, we must explicitly add it to admin
# This allows it to appear on the django administration dashboard

admin.site.register(Post)
