from django.urls import path
from . import views

app_name = 'restaurants'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:restaurant_id>/', views.detail, name='detail'),
    path('<int:restaurant_id>/favorites', views.favorites, name='favorites'),
    path('<int:restaurant_id>/reviews', views.reviews, name='reviews'),
    path('<int:restaurant_id>/reviews/<int:review_id>/likes', views.likes, name='likes')
]