from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from restaurants.models import Restaurant, Favorite, Review

def mypage(request):
    if request.user.is_anonymous:
        return redirect('/accounts/login')

    current_user = request.user

    favorite_list = Favorite.objects.select_related('restaurant').filter(user=current_user, status=1)
    review_list = Review.objects.select_related('restaurant').filter(user=current_user)
    
    return render(request, 'account/mypage.html', {'favorite_list': favorite_list, 'review_list': review_list})

def mypage_edit(request):
    if request.user.is_anonymous:
        return redirect('account/login')

    current_user = request.user

    return render(request, 'account/mypage_edit.html')

def mypage_update(request):
    if request.user.is_anonymous or request.method != 'POST':
        return redirect('/accounts/login')

    current_user = request.user

    name = request.POST.get("name")
    email = request.POST.get("email")

    current_user.username = name
    current_user.email = email
    current_user.save()

    return redirect('/accounts/mypage')

def detail(request, user_id=id):
    user = get_object_or_404(User, pk=user_id)

    favorite_list = Favorite.objects.select_related('restaurant').filter(user=user, status=1)
    review_list = Review.objects.select_related('restaurant').filter(user=user)

    return render(request, 'account/detail.html', {'user': user, 'favorite_list': favorite_list, 'review_list': review_list})
