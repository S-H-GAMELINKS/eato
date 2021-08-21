from django.shortcuts import render
from restaurants.models import Restaurant

def lp(request):
    restaurant_list = Restaurant.objects.order_by('?')[:9]
    return render(request, 'lp.html', {'restaurant_list': restaurant_list})
