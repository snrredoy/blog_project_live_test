from django.shortcuts import render, redirect
from .import forms
from .import models

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
    search_by = request.GET.get('search_by')
    
    if query:
        if search_by == 'title':
            results = models.Post.objects.filter(title__icontains=query)
        elif search_by == 'category':
            results = models.Post.objects.filter(category__icontains=query)
        else:
            results = models.Post.objects.none()
    else:
        results = models.Post.objects.all()
    
    return render(request, 'search_results.html', {'results': results, 'query': query, 'search_by': search_by})