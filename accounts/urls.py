from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.mypage, name='mypage'),
    path('_edit', views.mypage_edit, name='mypage_edit'),
    path('_update', views.mypage_update, name='mypage_update'),
]