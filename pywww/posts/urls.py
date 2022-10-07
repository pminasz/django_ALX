from django.urls import path
from posts.views import posts_list, posts_details, add_post_form, temp_1_inposts, toggle_sponsored

app_name = 'posts'

urlpatterns = [
   path('', posts_list, name='list'),
   path('add', add_post_form, name='add'),
   path('<int:id>', posts_details, name='details'),
   path('', posts_list, name='temp_1_inposts'),
   path('toggle_sponsored/<int:id>', toggle_sponsored, name='toggle_sponsored'),
]
