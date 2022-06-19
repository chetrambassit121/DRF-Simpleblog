from . import views
from django.urls import path, include

urlpatterns = [
    path('homepage/', views.homepage, name='posts_home'),
    path('', views.list_posts, name='list_posts'),
    path('<int:post_id>', views.post_detail, name='post_detail'),

]