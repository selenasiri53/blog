from django.urls import path
from .views import BlogListView, BlogDetailView # new

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), # new
    path('', BlogListView.as_view(), name='home'),
]

# each post detail url will start with 'post/'. then identify the specific post_detail by id or pk (primary key
# django automatically adds an auto-incrementing primary key