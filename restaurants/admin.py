from django.conf import settings
from django.utils.html import mark_safe
from django.contrib import admin
from .models import Restaurant, Favorite, Review, Like
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class RestaurantResource(resources.ModelResource):

    class Meta:
        model = Restaurant

class RestaurantAdmin(ImportExportModelAdmin):
    resource_class = RestaurantResource

    list_display = ('name', 'address', 'tel_number', 'favorites', 'reviews', 'image_tag')

    readonly_fields = ('favorites', 'reviews')

    def name(self, instance):
        return instance.name

    def address(self, instance):
        return instance.address

    def tel_number(self, instance):
        return instance.tel_number

    def favorites(self, instance):
        favorites = Favorite.objects.filter(restaurant=instance)
        return favorites.count()

    def reviews(self, instance):
        reviews = Review.objects.filter(restaurant=instance)
        return reviews.count()

    def image_tag(self, instance):
        return mark_safe('<img src="%s%s" height="150" class="img-fluid" />' % (settings.MEDIA_URL, instance.image))

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'user', 'content', 'likes')

    readonly_fields = ('likes',)

    def restaurant(self, instance):
        return instance.restaurant.name

    def user(self, instance):
        return instance.user.username

    def content(self, instance):
        return instance.content

    def likes(self, instance):
        return instance.like_set.count()

class LikeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Like, LikeAdmin)
