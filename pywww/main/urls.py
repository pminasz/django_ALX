from django.urls import path
from main.views import hello_world, contacts, contacts_2, contact, links


app_name = 'main'
urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('contacts', contacts, name='contacts'),
    path('contacts_2', contacts_2, name='contacts_2'),
    path('contact', contact, name="contact"),
    path('links', links, name="links"),
]