from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Post
from group.models import Group


# Create your views here.
def index(request):
    latest = Post.objects.order_by('-pub_date')[:10]
    # возвращаем результат выполнения функции render
    return render(request, "index.html", {"posts": latest})


def group_post(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    return render(request, "group.html", {"group": group, "posts": posts})
