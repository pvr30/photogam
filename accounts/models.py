from django.db import models
from django.contrib.auth.models import AbstractUser
from crum import get_current_user # external library for get current user

# Create your models here.

class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics/%Y/%m/%d', blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

    @property
    def get_followers_count(self):
        return UserFollowers.objects.filter(follower=self.id).count()



# followers of user
class UserFollowers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userfollower", editable=False)
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    followed_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # get_current logged in user using django-crums library
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        self.modified_by = user
        super(UserFollowers, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.user} followed {self.follower}"




