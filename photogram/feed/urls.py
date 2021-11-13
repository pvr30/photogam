from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('profile', views.profile, name="profile"),
    
    path('post/<int:id>', views.post_detail, name="postdetail"),
    path('comment/<int:id>/', views.comment, name="comment"),
    path('like/<int:id>/', views.like, name="like"),
    path('unlike/<int:id>/', views.unlike, name="unlike"),

    path('profile/<int:id>', views.profile_of_other_user, name="profile_of_other_user"),

    path('follow/<int:id>', views.follow, name="follow"),
    path('unfollow/<int:id>', views.unfollow, name="unfollow"),

]