import os
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from restaurants.models import Restaurant, Favorite, Review
from accounts.models import Profile

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
    bio = request.POST.get("bio")

    icon = request.FILES.get("icon")

    if icon is not None:
        if os.getenv('APP_ENV') == 'production':
            save_icon = default_storage.save(icon.name, icon)
            uploaded_file_url = f'{settings.MEDIA_URL}{save_icon}'
        else:
            fs = FileSystemStorage()
            filename = fs.save(icon.name, icon)
            uploaded_file_url = fs.url(filename)

        current_user.profile.icon = uploaded_file_url

    current_user.username = name
    current_user.email = email
    current_user.profile.bio = bio
    current_user.save()

    return redirect('/accounts/mypage')

def detail(request, user_id=id):
    user = get_object_or_404(User, pk=user_id)

    favorite_list = Favorite.objects.select_related('restaurant').filter(user=user, status=1)
    review_list = Review.objects.select_related('restaurant').filter(user=user)

    return render(request, 'account/detail.html', {'user': user, 'favorite_list': favorite_list, 'review_list': review_list})
