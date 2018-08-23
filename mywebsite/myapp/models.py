from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# we will inhert from built in User (authintcations user)by defult it has first name/lastname/email/password


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # additional filed isn't inhert form User
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    # this will uplode userprofile pic to directroy (media) profile_pics

    # this is bulit in user
    def __str__(self):
        return self.user.username
