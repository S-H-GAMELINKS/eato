from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Restaurant, Favorite

def index(request):
    r_list = Restaurant.objects.all()

    paginator = Paginator(r_list, 12)

    page_number = request.GET.get('page')
    r_page_obj = paginator.get_page(page_number)

    context = {'restaurant_list': r_page_obj}
    return render(request, 'restaurants/index.html', context)

def detail(request, restaurant_id=id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    if request.user.is_authenticated:
        current_user = request.user
        favorite = Favorite.objects.filter(user=current_user, restaurant=restaurant).first()
        return render(request, 'restaurants/detail.html', {'restaurant': restaurant, 'current_user': current_user, 'favorite': favorite})
    else:
        return render(request, 'restaurants/detail.html', {'restaurant': restaurant})

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
