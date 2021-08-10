from django.urls import path, include
from blog.views import PostViewSet

post_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

post_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('posts/', post_list, name='posts-list'),
    path('posts/<int:pk>/', post_detail, name='post-details')
]