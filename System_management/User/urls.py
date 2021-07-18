from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register),
    path('login', views.login_user),
    path('logout', views.logout_user),
    path('post_add',views.post_add),
]
