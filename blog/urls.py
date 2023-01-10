from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('category/<slug:slug>/', views.PostsbyCategory.as_view(), name='category'),
    path('tag/<slug:slug>/', views.PostsbyTag.as_view(), name='tag'),
    path('post/<slug:slug>/', views.GetPost.as_view(), name='post'),
    path('search/', views.Search.as_view(), name='search')
]
