from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView # new

urlpatterns = [
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'), 
    path('post/new/', BlogCreateView.as_view(), name='post_new'), 
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]

# each post detail url will start with 'post/'. then identify the specific post_detail by id or pk (primary key
# django automatically adds an auto-incrementing primary key