from django.db import models
from django.db.models import Model
from django.utils.timezone import now

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 20)
    username = models.CharField(max_length = 20, primary_key = True)

    def __str__(self):
        return self.username

    class Meta:
        app_label = 'User'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = "User"

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'User'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'Post'