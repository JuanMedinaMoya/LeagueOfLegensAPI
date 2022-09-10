from django.urls import path, include
from . import views

urlpatterns = [
    path ('', views.index, name='index'),
    path('player/',views.player, name = 'player'),
    path('player/<str:pk>/',views.getplayer, name='player'),
    path('friends/',views.friends,name='friends'),
    path('accounts/', include('accounts.urls'))
]