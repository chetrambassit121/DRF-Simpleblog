from . import views
from django.urls import path, include

urlpatterns = [
    path('homepage/', views.homepage, name='posts_home'),
]