from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, DestinationsPost, PracticalPost, OtherPost, Comment
from .forms import PostForm, DestPostForm, PracPostForm, OtherPostForm, CommentForm
from django.contrib.auth.decorators import login_required


def post_list(request):
    d_posts = DestinationsPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:3]
    p_posts = PracticalPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:3]
    o_posts = OtherPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:3]
    return render(request, 'forum/post_list.html', {'d_posts': d_posts, 'p_posts': p_posts, 'o_posts': o_posts})


def post_list_dest(request):
    posts = DestinationsPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'forum/post_list_dest.html', {'posts': posts})


def post_list_prac(request):
    posts = PracticalPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'forum/post_list_prac.html', {'posts': posts})


def post_list_other(request):
    posts = OtherPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'forum/post_list_other.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'forum/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'forum/post_edit.html', {'form': form})


@login_required
def dest_post_new(request):
    if request.method == "POST":
        form = DestPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            post.save()
            return redirect('dest_post_detail', pk=post.pk)
    else:
        form = DestPostForm()
    return render(request, 'forum/post_edit.html', {'form': form})


@login_required
def prac_post_new(request):
    if request.method == "POST":
        form = PracPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            post.save()
            return redirect('prac_post_detail', pk=post.pk)
    else:
        form = PracPostForm()
    return render(request, 'forum/post_edit.html', {'form': form})


@login_required
def other_post_new(request):
    if request.method == "POST":
        form = OtherPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            post.save()
            return redirect('other_post_detail', pk=post.pk)
    else:
        form = DestPostForm()
    return render(request, 'forum/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'forum/post_edit.html', {'form': form})


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'forum/add_comment_to_post.html', {'form': form})


@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'forum/post_draft_list.html', {'posts': posts})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
