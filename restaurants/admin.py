from django.contrib import admin
from .models import Restaurant, Favorite

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'tel_number', 'favorites',)

    readonly_fields = ('favorites', )

    def name(self, instance):
        return instance.name

    def address(self, instance):
        return instance.address

    def tel_number(self, instance):
        return instance.tel_number

    def favorites(self, instance):
        favorites = Favorite.objects.filter(restaurant=instance)
        return favorites.count()

admin.site.register(Restaurant, RestaurantAdmin)
