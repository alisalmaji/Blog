from django.shortcuts import render
from rest_framework import viewsets
from blog.models import Post
from blog.serializers import PostSerializer, PostShareSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from blog.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from django.core.mail import send_mail


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'posts': reverse('blog:posts-list', request=request, format=format)
    })


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'share_with_email':
            return PostShareSerializer
        else:
            return PostSerializer

    @action(detail=False, methods=['POST'])
    def share_with_email(self, request, pk, *args, **kwargs):
        ser = PostShareSerializer(data=request.data)

        if ser.is_valid():
            post = Post.objects.get(id=pk)
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{ser.validated_data['name']} recommends you read" \
                      f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                      f"{ser.validated_data['comments']}"
            send_mail(subject, message, 'alisalmajialisalmaji@gmail.com', [ser.validated_data['to']])
            return Response(ser.validated_data)

