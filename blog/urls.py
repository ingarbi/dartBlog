from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('category/<slug:slug>/', views.get_category, name='category'),
    path('post/<slug:slug>/', views.get_post, name='post')
]
