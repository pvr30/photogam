from django.db import models
from django.contrib.auth import get_user_model
from crum import get_current_user
# from accounts.models import User
# Create your models here.

User = get_user_model()

# posts of user
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    pic = models.FileField(upload_to="feed_posts/%Y/%m/%d")
    caption = models.CharField(max_length=200, blank=True, null=True)
    likes = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    
    # get_current logged in user using django-crums library
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        self.modified_by = user
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}"
    
    @property
    def likes_count(self):
        return Like.objects.filter(post=self.id).count()
    
    @property
    def comments_count(self):
        return Comment.objects.filter(post=self.id).count()


def get_posts_count(user):
    return Post.objects.filter(user=user).count()

    
# comment on a post
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, null=True, blank=True)
    likes_on_comment = models.IntegerField(default=0)
    commented_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        self.modified_by = user
        super(Comment, self).save(*args, **kwargs)
        
    def __str__(self) -> str:
        return f"Comment:{self.id} on Post:{self.post.id}"

    

# likes
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        self.modified_by = user
        super(Like, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.user}->{self.post}"