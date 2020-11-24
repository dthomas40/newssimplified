from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('external/', views.external),
    path('about/', views.about, name='blog-about'),
    path('', views.button)
]