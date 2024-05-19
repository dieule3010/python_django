from django.urls import path
from . import views

urlpatterns = [
   path('', views.index),
   path('a/', views.helo),
   path('dieu/',views.dieu)
]