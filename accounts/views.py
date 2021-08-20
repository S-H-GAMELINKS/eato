from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from restaurants.models import Restaurant, Favorite

def mypage(request):
    if request.user.is_anonymous:
        return redirect('/accounts/login')

    current_user = request.user

    favorite_list = Favorite.objects.select_related('restaurant').filter(user=current_user, status=1)
    
    return render(request, 'account/mypage.html', {'favorite_list': favorite_list})
