from django.shortcuts import render, redirect
from .import forms
from .import models
from django.db.models import Q

def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
        
    else:
        post_form = forms.PostForm()
        
    return render(request, 'add_post.html',{'form': post_form})


def edit_post(request, id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
        
    else:
        post_form = forms.PostForm()
        
    return render(request, 'add_post.html',{'form': post_form})

def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    
    return redirect ('homepage')

def search_post(request):
    query = request.GET.get('q')
    print(query)
    
    if query:
        posts = models.Post.objects.filter(Q(title__icontains=query) | Q(category__name__icontains=query))
    else:
        posts = models.Post.objects.all()
    
    return render(request, 'search_results.html', {'posts': posts, 'query': query,})