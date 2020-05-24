from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish"),
    (2,"Scheduled")
)

class Category(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    item = models.CharField(max_length=200, unique=True)
    cost = models.CharField(max_length=50, default='OBO')
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    categories = models.ManyToManyField('Category', related_name='posts')

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.item