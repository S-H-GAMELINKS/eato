from django.shortcuts import render
from restaurants.models import Restaurant, Review
from django .views.generic import TemplateView

def lp(request):
    restaurant_list = Restaurant.objects.order_by('?')[:9]
    review_list = Review.objects.select_related('restaurant').order_by('?')[:9]
    return render(request, 'lp.html', {'restaurant_list': restaurant_list, 'review_list': review_list})

class PrivacyClass(TemplateView):
    template_name = 'privacy.html';

class TermsClass(TemplateView):
    template_name = 'terms.html';
