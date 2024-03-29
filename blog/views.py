from django.shortcuts import render
from .models import Post
from django.shortcuts import redirect
from django.contrib import auth

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def list(request):
    postList=Post.objects.all()
    return render(request, 'blog/list.html', {'postList':postList})

def view(request, pk):
    post=Post.objects.get(pk=pk)
    return render(request, 'blog/view.html', {'post':post})

def write(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            new_article=Post.objects.create(
                author=request.user,
                title=request.POST['title'],
                text=request.POST['text'],
            )
            return redirect('/list/')
        
        return render(request, 'blog/write.html')
    return redirect('/admin/')