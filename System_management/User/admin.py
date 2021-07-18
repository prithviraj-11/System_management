from django.contrib import admin
from .models import User, Post

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'email', 'password', 'username']
    
    class Meta:
        model = User


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user','text','created_at','updated_at']

    class Meta:
        model = Post