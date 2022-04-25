from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm

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


@login_required
def new_post(request):
    error = ""
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("index")
        else:
            error = "Форма содержит ошибки"
        return render(request, "new.html", {"form": form})
    form = PostForm()
    return render(request, "new.html", {"form": form})
