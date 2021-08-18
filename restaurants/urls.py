from django.urls import path
from . import views

app_name = 'restaurants'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:restaurant_id>/', views.detail, name='detail'),
    path('<int:restaurant_id>/favorites', views.favorites, name='favorites'),
]