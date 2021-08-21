from django.contrib import admin
from .models import Restaurant, Favorite
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class RestaurantResource(resources.ModelResource):

    class Meta:
        model = Restaurant

class RestaurantAdmin(ImportExportModelAdmin):
    resource_class = RestaurantResource

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
