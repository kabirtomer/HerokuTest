from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView, DetailView, edit
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import NewPostForm
from django.http import HttpResponse

class BlogListView(ListView):
    model=Post
    template_name='blogs.html'

class BlogDetailView(DetailView):
    model=Post
    template_name = 'post_detail.html'

class BlogCreateView(edit.CreateView):
    model=Post
    template_name='post_new.html'
    fields='__all__'

class BlogEditView(edit.UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['text']

class BlogDeleteView(edit.DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url=reverse_lazy('blogs')

class SignUpView(edit.CreateView):
    form_class = UserCreationForm
    success_url= reverse_lazy('login')
    template_name='signup.html'

def new_topic(request):
    user=request.user
    object_list=Post.objects.all()
    if request.method == 'POST':
        form= NewPostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=user
            post.title=''
            post.save()
            return redirect('blogs')
    else:
        form = NewPostForm()
    return render(request, 'blogs.html', {'form' : form, 'object_list' : object_list})