from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

POSTS_PER_PAGE = 3
# Create your views here.
def post(request):
    all_posts = Post.objects.order_by('-published_date')

    paginator = Paginator(all_posts, POSTS_PER_PAGE)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    hot_posts = Post.objects.filter(hot=True).order_by('-published_date')
    most_posts = Post.objects.filter(most=True).order_by('-published_date')
    popular_posts = Post.objects.filter(popular=True).order_by('-published_date')
    context = {
        'posts': posts,
        'hot_posts': hot_posts,
        'most_posts': most_posts,
        'popular_posts' : popular_posts,
    }
    return render(request, 'posting/post.html', context)