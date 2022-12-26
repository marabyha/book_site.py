from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('genres/', views.genres, name = 'genres'),
    path('genres/boevik/', views.boevik, name='boevik'),
    path('genres/boevik/1/', views.boevik1, name = 'boevik1'),
    path('genres/boevik/2/', views.boevik2, name = 'boevik2'),
    path('genres/boevik/3/', views.boevik3, name = 'boevik3'),
    path('genres/detectiv/', views.detectiv, name = 'detectiv'),
    path('genres/detectiv/1/', views.detectiv1, name = 'detectiv1'),
    path('genres/detectiv/2/', views.detectiv2, name = 'detectiv2'),
    path('genres/detectiv/3/', views.detectiv3, name = 'detectiv3'),
    path('genres/istroman/', views.istroman, name = 'istroman'),
    path('genres/istroman/1/', views.istroman1, name = 'istroman1'),
    path('genres/istroman/2/', views.istroman2, name = 'istroman2'),
    path('genres/istroman/3/', views.istroman3, name = 'istroman3'),
    path('genres/lubroman/', views.lubroman, name = 'lubroman'),
    path('genres/lubroman/1/', views.lubroman1, name = 'lubroman1'),
    path('genres/lubroman/2/', views.lubroman2, name = 'lubroman2'),
    path('genres/lubroman/3/', views.lubroman3, name = 'lubroman3'),
    path('genres/triller/', views.triller, name = 'triller'),
    path('genres/triller/1/', views.triller1, name = 'triller1'),
    path('genres/triller/2/', views.triller2, name = 'triller2'),
    path('genres/triller/3/', views.triller3, name = 'triller3'),
]
