from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('world/', views.world, name='blog-world'),
    path('finance/', views.finance, name='blog-finance'),
    path('politics/', views.politics, name='blog-politics'),
    path('s&t/', views.science, name='blog-science'),
    path('health/', views.health, name='blog-health'),
    path('entertainment/', views.entertainment, name='blog-entertainment'),
    path('external/', views.external),
    path('button/', views.button),
    path('about/', views.about, name='blog-about'),
    path('', views.button)
]