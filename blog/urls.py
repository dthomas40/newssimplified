from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('world/', views.world, name='blog-world'),
    path('external/', views.external),
    path('button/', views.button),
    path('about/', views.about, name='blog-about'),
    path('', views.button)
]