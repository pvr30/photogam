from django.shortcuts import get_object_or_404, redirect, render

from accounts.models import User, UserFollowers
from .models import Comment, Like, Post, get_posts_count
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    posts = Post.objects.all()

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(request.META.get('HTTP_REFERER'))


    data = {
        'posts': posts,
        'form': form,
    }
    return render(request, 'feed/home.html', data)

    
@login_required(login_url='login')
def profile(request):
    posts = Post.objects.filter(user=request.user)
    post_count = get_posts_count(user=request.user)
    data = {
        'posts': posts,
        'post_count': post_count,
    }
    return render(request, 'accounts/profile.html', data)


# post detail
@login_required(login_url='login')
def post_detail(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post)

    try:
        Like.objects.get(user=request.user, post=post)
        like_value = True
    except:
        like_value = False

    data = {
        'post': post, 
        'like_value': like_value,
        'comments': comments,
    }
    return render(request, 'feed/post_detail.html', data)


@login_required(login_url='login')
def profile_of_other_user(request, id):
    user_ = User.objects.get(id=id)
    posts = Post.objects.filter(user=user_)
    post_count = get_posts_count(user=user_)
    print(user_.get_followers_count)
    if request.user.id == id:
        return redirect('profile')

    try:
        UserFollowers.objects.get(follower=user_)
        follow_val = True
    except:
        follow_val = False

    data = {
        'user_':user_,
        'posts': posts,
        'post_count': post_count,
        'follow_val': follow_val,
    }
    return render(request, 'feed/profile_user.html', data)

# comment on post
@login_required(login_url='login')
def comment(request, id):
    if request.method == 'POST':
        comment = request.POST['comment']
        if comment == "":
            return redirect(request.META.get('HTTP_REFERER'))
        post = get_object_or_404(Post, id=id)
        comment_post = Comment(post=post, comment=comment)
        # print(post)
        comment_post.save()
    return redirect(request.META.get('HTTP_REFERER'))

# like 
@login_required(login_url='login')
def like(request, id):
    post = Post.objects.get(id=id)

    try:
        Like.objects.get(user=request.user, post=post)
    except:
        Like.objects.create(post=post)

    return redirect(request.META.get('HTTP_REFERER'))
    
# dislike
@login_required(login_url='login')
def unlike(request, id):
    post = Post.objects.get(id=id)
    
    try:
        like_obj = Like.objects.get(user=request.user, post=post)
        like_obj.delete()
    except:
        pass

    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def follow(request, id):
    user = User.objects.get(id=id)

    try:
        UserFollowers.objects.get(follower=user)
    except:
        UserFollowers.objects.create(follower=user)
        

    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def unfollow(request, id):
    user = User.objects.get(id=id)

    try:
        follower = UserFollowers.objects.get(follower=user)
        follower.delete()
    except:
        UserFollowers.objects.create(follower=user)

    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='login')  
def deletepost(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return redirect('home')
    except:
        return redirect(request.META.get('HTTP_REFERER'))

    
