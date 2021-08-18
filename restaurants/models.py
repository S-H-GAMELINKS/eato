from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    tel_number = models.CharField(max_length=20)

class Favorite(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    status = models.IntegerField(null=True)

    def is_favorited(self, user, restaurant):
        if self.user == user and self.restaurant == restaurant and self.status != 0:
            return True
        else:
            return False

    def favorite(self):
        self.status = 1
        self.save()

    def unfavorite(self):
        self.status = 0
        self.save()
