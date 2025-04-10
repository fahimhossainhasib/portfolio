from django.shortcuts import render
from .models import Portfolio, Blog 

def home(request):
    recent_posts = Blog.objects.order_by('-published_at')
    return render(request, 'home.html', {'recent_posts': recent_posts[:3]})

def portfolio(request):
    return render(request, 'portfolio.html')

def blog(request):
    blog_posts = Blog.objects.all()
    return render(request, 'blog.html', {'blog_posts': blog_posts})

def read_post(request, post_id):
    post = Blog.objects.get(id=post_id)
    return render(request, 'read_post.html', {'post': post})
