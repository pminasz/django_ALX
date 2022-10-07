from django.shortcuts import render
from django.http import HttpRequest
from posts.models import Post
from main.forms import ContactForm

# Create your views here.
def hello_world(request: HttpRequest):
    context = {}
    return render(request, 'main/hello.html', context)

def links(request: HttpRequest):
    context = {}
    return render(request, 'main/links.html', context)

def contacts(request: HttpRequest):
    context = {}
    return render(request, 'main/contacts.html', context)


def contacts_2(request: HttpRequest):
    context = {}
    return render(request, 'main/contacts_2.html', context)

def contact(request: HttpRequest):
    if request.method == 'POST':
        # odbiór danych
        dane_f_formularza = request.POST
        f = ContactForm(request.POST)
        f.is_valid()
        print(f.cleaned_data)
        print(f.cleaned_data)
        print(f.cleaned_data)
        ...
    else:
        context = {'form': ContactForm}
        return render(request, 'main/contact.html', context)




