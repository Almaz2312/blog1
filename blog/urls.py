from django.urls import path
from . import views
# from .views import all_blogs
# from .views import *


urlpatterns = [
    path('', views.all_blogs, name='blogs'),
    path('create/', views.create_blog, name='create'),
    path('detail/<int:pk>/', views.detail_blog, name='details'),
    path('edit/<int:pk>/', views.edit_blog, name='edit'),
    path('delete/<int:pk>/', views.delete_blog, name='delete'),
]

