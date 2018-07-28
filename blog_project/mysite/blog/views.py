from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin  #to mixin ...auth for class basd views
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from blog.forms import PostForm,CommentForm
from django.views.generic import (View,TemplateView,ListView,DetailView, #import for class based views
                                    CreateView,UpdateView,DeleteView)
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'


class PostListView(ListView):
    model = Post

    def get_queryset(self):  #SQL query in python
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post

# Reminder
# CreateView class added in views.py
# Error1 : ImproperlyConfigured at /basic_app/create
# Using ModelFormMixin (base class of SchoolCreateView) without the 'fields' attribute is prohibited.
#Here we want to create new entries in DB but we also want some authorisation...as we dont want
#anyone to update the DB...
#will use mixins ( the decorators used previously)
class CreatePostView(LoginRequiredMixin,CreateView):
    #some defaut variables that we have to setup
    login_url = '/login/'  #where should the user go.
    redirect_field_name = 'blog/post_detail.html'  #after log in take them to detail view
    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin,UpdateView):
    #some defaut variables that we have to setup
    login_url = '/login/'  #where should the user go.
    redirect_field_name = 'blog/post_detail.html'  #after log in take them to detail view
    form_class = PostForm
    model = Post


class PostRemoveView(LoginRequiredMixin,DeleteView):
    model = Post
    # we have to make sure that the post is deleted then take the user where ever we want so for that
    # we do lazyreverse
    reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post
    def get_queryset(self):  #SQL query in python
        return Post.objects.filter(published_date__isnull=True).orderby('created_date')


#################################################

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request == POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)

    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})


@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approved()
    return redirect('post.detail',pk=comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk #just remembering the pk so that we know abt it once its deleted
    comment.delete()
    return redirect ('post.detail',pk=post_pk)
