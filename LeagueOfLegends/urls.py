from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    path('player',views.player, name = 'player'),
    path('player/<str:pk>/',views.player, name='player'),
    path('login', views.login, name ='login'),
    path('register',views.register,name='register'),
    path('friends',views.friends,name='friends')
]