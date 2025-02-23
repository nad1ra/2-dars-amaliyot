from django.db import models
from django.db.models import CASCADE


class Author(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    bio = models.TextField()

class Category(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)
    desc = models.TextField()

class Tag(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(unique=True)

class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=CASCADE)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=50)
    author_email = models.EmailField(unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)






