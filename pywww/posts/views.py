from pprint import pprint
from django.http import HttpResponse
from posts.models import Post
from django.shortcuts import render
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from tags.models import Tag


def posts_list(request):
    q = title__contains = request.GET.get('q')
    lista_postow = Post.objects.all()
    if q:
        lista_postow = lista_postow.filter(title__contains=q)
    context = {'imie': 'Jan',
               'nazwisko': 'Kowalski',
               'samochod': 'Mercedes-Benz',
               'model': 'G1 (W103)',
               'posts_list': lista_postow}
    lista_postow = lista_postow.order_by('-sponsored')
    context = {
        'posts_list': lista_postow,
    }
    return render(request, 'posts/list.html', context)


def posts_details(request, id):
    p = Post.objects.get(id=id)
    context = {'post': p}
    return render(request, 'posts/details.html', context)

def toggle_sponsored(request, id):
    post = Post.objects.get(id=id)
    post.sponsored = not post.sponsored
    post.save()
    return redirect('posts:list')

def add_post_form(request):
    if request.method == "POST":
        pprint(dict(request.POST))
        data = {
            "title": request.POST['title'],
            "content": request.POST['content'],
            "published": 'published' in request.POST,
            "author": User.objects.first()
        }
        post = Post.objects.create(**data)
        for tag_id in request.POST.getlist('tags'):
            tag_id = int(tag_id)
            t = Tag.objects.get(id=tag_id)
            post.tags.add(t)
        return redirect('posts:list')
    else:
        # wczytać tagi
        # dodać do kontekstu
        context = {
            'tags': Tag.objects.all(),
            'authors' : User.objects.all(),
        }
        return render(request, 'posts/add.html', context)


def temp_1_inposts(request, id):
    ...
