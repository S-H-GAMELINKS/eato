from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('mypage', views.mypage, name='mypage'),
    path('mypage_edit', views.mypage_edit, name='mypage_edit'),
    path('mypage_update', views.mypage_update, name='mypage_update'),
    path('<int:user_id>', views.detail, name='detail')
]