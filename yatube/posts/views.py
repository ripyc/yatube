from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import PostForm

from .models import Post, User
from group.models import Group


# Create your views here.
def index(request):
    post_list = Post.objects.order_by('-pub_date').all()
    paginator = Paginator(post_list, 10)  # показывать по 10 записей на странице.

    page_number = request.GET.get('page')  # переменная в URL с номером запрошенной страницы
    page = paginator.get_page(page_number)  # получить записи с нужным смещением
    return render(request, 'index.html', {'page': page, 'paginator': paginator})


def group_post(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = Post.objects.filter(group=group).order_by("-pub_date").all()
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, "group.html", {"group": group, 'page': page, 'paginator': paginator})


@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("index")
        return render(request, "new.html", {"form": form, "editing": False})
    form = PostForm()
    return render(request, "new.html", {"form": form, "editing": False})


def profile(request, username):
    author = get_object_or_404(User, username=username)
    post_list = Post.objects.filter(author=author).order_by("-pub_date").all()
    total_posts = post_list.count
    if not Post.objects.filter(author=author).exists():
        post_list = ['пока нет записей']
        total_posts = 0
    last_post = post_list[0]
    paginator = Paginator(post_list[1:], 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(
        request,
        'profile.html',
        {'author': author,
         'last_post': last_post,
         'total_posts': total_posts,
         'page': page,
         'paginator': paginator
    })


def post_view(request, username, post_id):
    author = get_object_or_404(User, username=username)
    post_list = Post.objects.filter(author=author).order_by("pub_date").all()
    return render(
        request,
        'post.html',
        {'author': author,
         'post_id': post_id,
         'post': post_list[post_id-1],
         'total_posts': post_list.count
    })


@login_required
def post_edit(request, username, post_id):
    author = get_object_or_404(User, username=username)
    post = Post.objects.filter(author=author).order_by("pub_date")[post_id-1]
    if request.method == "GET":
        # проверяем, что текущий пользователь это автор поста
        if str(request.user) != username:
            return redirect('post', username=username, post_id=post_id)
        form = PostForm(instance=post)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            #post = form.save(commit=False)
            #post.author = request.user
            form.save()
        return redirect('post', username=username, post_id=post_id)
    return render(
        request,
        "new.html",
        {"form": form,
         "author": username,
         "post_id": post_id,
         "editing": True})

