from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.order_by('-published_date')  # Orders newest first
    return render(request, 'blog/post_list.html', {'posts': posts})