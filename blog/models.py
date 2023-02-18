from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    # possible to make the 'author' field optional if we want later
    body = models.TextField()

    def __str__(self):
        return self.title

# ForeignKey - many-to-one; a user can be the author of many blog posts, but not the other way around
# ^ must specify on_delete

# List of django fields:
# https://docs.djangoproject.com/en/3.1/topics/db/models/#fields