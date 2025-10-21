from django.shortcuts import render
from .models import Post  # import your model

def post_list(request):
    posts = Post.objects.all().order_by('published_date')  # ORM QuerySet
    return render(request, 'blog/post_list.html', {'posts': posts})
