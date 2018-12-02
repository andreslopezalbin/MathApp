from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('play/', views.init, name='init'),
    path('play/second/', views.play, name='second'),

]
