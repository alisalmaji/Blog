from django.urls import path, include
from blog.views import PostViewSet, api_root, share_with_email
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'blog'  # so important to use blog:post-detail in other apps or either other files in this app

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

post_share = share_with_email

urlpatterns = [
    path('', api_root),
    path('posts/', post_list, name='posts-list'),
    path('posts/<int:pk>/', post_detail, name='post-details'),
    path('posts/share/<int:pk>', post_share, name='post-share')
]

# urlpatterns += [      # when add app_name to this urls.py, browsable api login not worked. put this in main urls.py
#     path('api-auth/', include('rest_framework.urls')),
# ]

urlpatterns = format_suffix_patterns(urlpatterns)
