from django.shortcuts import render
from .models import Project
from blog.models import Post


def home(request):
    projects = Project.objects.all().order_by("-pk")
    blog_posts = Post.objects.all().order_by("-date", "-pk")[:3]
    context = {
        "projects": projects,
        "blog_posts": blog_posts,
        "blog_posts_count": Post.objects.count(),
    }
    return render(request, "home.html", context)
