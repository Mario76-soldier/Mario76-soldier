from django.shortcuts import render
from .models import Post
from django.shortcuts import redirect
from django.contrib import auth
import bcrypt
from django.http import HttpResponse

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
    if request.method=='POST':
        new_article=Post.objects.create(
            author=request.POST['author'],
            title=request.POST['title'],
            text=request.POST['text'],
            password=bcrypt.hashpw(request.POST['password'].encode("utf-8"), bcrypt.gensalt()).decode('utf-8'),
        )
        return redirect('/list/')    
    return render(request, 'blog/write.html')

def edit(request, pk):
    if request.method=='POST':
        post=Post.objects.get(pk=pk)
        if bcrypt.checkpw(request.POST['password'].encode('utf-8'), post.password.encode('utf-8')):
            post.title=request.POST['title']
            post.text=request.POST['text']
            post.save()
            post.publish()
        return redirect('/list/')
    post=Post.objects.get(pk=pk)
    return render(request, 'blog/edit.html', {'post':post})

def delete(request, pk):
    if request.method=='POST':
        post=Post.objects.get(pk=pk)
        if bcrypt.checkpw(request.POST['password'].encode('utf-8'), post.password.encode('utf-8')):
            post.delete()
            return HttpResponse(1)
        return HttpResponse(0)