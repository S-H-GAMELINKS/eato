import os
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Restaurant, Favorite, Review, ReviewImage, Like

def index(request):
    keyword = request.GET.get('keyword')

    if keyword:
        r_list = Restaurant.objects.order_by('id').filter(name__icontains=keyword)
    else:
        r_list = Restaurant.objects.order_by('id').all()

    paginator = Paginator(r_list, 12)

    page_number = request.GET.get('page')
    r_page_obj = paginator.get_page(page_number)

    context = {'restaurant_list': r_page_obj, 'keyword': keyword}
    return render(request, 'restaurants/index.html', context)

def detail(request, restaurant_id=id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    review_list = Review.objects.filter(restaurant=restaurant)

    if request.user.is_authenticated:
        current_user = request.user
        favorite = Favorite.objects.filter(user=current_user, restaurant=restaurant).first()
        return render(request, 'restaurants/detail.html', {'restaurant': restaurant, 'current_user': current_user, 'favorite': favorite, 'review_list': review_list})
    else:
        return render(request, 'restaurants/detail.html', {'restaurant': restaurant, 'review_list': review_list})

def favorites(request, restaurant_id=id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    if request.method == "POST":
        current_user = request.user

        if request.user.is_anonymous:
            return redirect('restaurants:detail', restaurant_id=restaurant.id)

        filter = Favorite.objects.filter(user=current_user, restaurant=restaurant)

        if filter.count() > 0:
            fav = filter.first()
            if fav.is_favorited(current_user, restaurant):
                fav.unfavorite()
            else:
                fav.favorite()
        else:
            fav = Favorite(user=current_user, restaurant=restaurant, status=1)
            fav.save()

        return redirect('restaurants:detail', restaurant_id=restaurant.id)
    else:
        return redirect('restaurants:detail', restaurant_id=restaurant.id)

def reviews(request, restaurant_id=id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    if request.method == "POST":
        current_user = request.user

        if request.user.is_anonymous:
            return redirect('restaurants:detail', restaurant_id=restaurant.id)

        review_image = request.FILES.get("review_image")

        if review_image is not None:
            if os.getenv('APP_ENV') == 'production':
                save_review_image = default_storage.save(review_image.name, review_image)
                uploaded_file_url = f'{settings.MEDIA_URL}{save_review_image}'
            else:
                fs = FileSystemStorage()
                filename = fs.save(review_image.name, review_image)
                uploaded_file_url = fs.url(filename)

        review = Review.objects.create(user=current_user, restaurant=restaurant, content=request.POST.get('content'), score=request.POST.get('score'))
        review.save()

        if review_image is not None:
            review_image = ReviewImage.objects.create(user=current_user, restaurant=restaurant, review=review, image=uploaded_file_url)
            review_image.save()

        return redirect('restaurants:detail', restaurant_id=restaurant.id)
    else:
        return redirect('restaurants:detail', restaurant_id=restaurant.id)

def likes(request, restaurant_id=id, review_id=id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    review = get_object_or_404(Review, pk=review_id)

    if request.method == "POST":
        current_user = request.user

        if request.user.is_anonymous:
            return redirect('restaurants:detail', restaurant_id=restaurant.id)

        filter = Like.objects.filter(user=current_user, restaurant=restaurant, review=review)

        if filter.count() > 0:
            like = filter.first()
            if like.is_liked(current_user, restaurant, review):
                like.unlike()
            else:
                like.like()
        else:
            like = Like(user=current_user, restaurant=restaurant, review=review, status=1)
            like.save()

        return redirect('restaurants:detail', restaurant_id=restaurant.id)
    else:
        return redirect('restaurants:detail', restaurant_id=restaurant.id)

def search_with_current_location(request):
    restaurants_list = Restaurant.objects.order_by('id').filter(latitude__isnull=False,longitude__isnull=False)
    result_list = []

    range = float(request.GET.get("range"))

    user_location_info = (request.GET.get("latitude"), request.GET.get("longitude"))

    for restaurant in restaurants_list:
        if restaurant.check_distance(user_location_info, range):
            result_list.append(restaurant)
    
    return render(request, 'restaurants/search_with_current_location.html', {'restaurant_list': result_list})
