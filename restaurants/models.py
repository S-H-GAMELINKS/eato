from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    tel_number = models.CharField(max_length=20)
    image = models.ImageField(null=True)

    class Meta:
        verbose_name_plural = "飲食店"

class Favorite(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    status = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = "お気に入り"

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

class Review(models.Model):
    content = models.TextField(max_length=500)
    score = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def is_liked(self, user):
        like = self.like_set.filter(user=user).first()

        if like.status != 0:
            return True
        else:
            return False

    def score_star(self):
        MAX_SCORE = 5

        if self.score != 0:
            return "★" * self.score + "☆" * (MAX_SCORE - self.score)
        else:
            return "☆" * MAX_SCORE

class Like(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True)
    status = models.IntegerField(null=True)

    def is_liked(self, user, restaurant, review):
        if self.user == user and self.restaurant == restaurant and self.review == review and self.status != 0:
            return True
        else:
            return False

    def like(self):
        self.status = 1
        self.save()

    def unlike(self):
        self.status = 0
        self.save()
