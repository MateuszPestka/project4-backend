from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer


class PostList(APIView):
    def get(slef, request):
        posts = Post.objects.all()
        serializer = PostSerializer(
            posts, many=True, contect={'request': request}
        )
        return Response(serializer.data)
