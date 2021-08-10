from django.shortcuts import render, get_object_or_404
from .models import Restaurant

def index(request):
    r_list = Restaurant.objects.all()
    context = {'restaurant_list': r_list}
    return render(request, 'restaurants/index.html', context)

def detail(request, restaurant_id=id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    return render(request, 'restaurants/detail.html', {'restaurant': restaurant})
