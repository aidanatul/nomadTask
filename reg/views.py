from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.serializers import serialize
from reg.models import Post, Comment
from reg.serializers import PostSerializer, CommentSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        try:
            post = Post.objects.get(pk=self.request.data['pk'])
        except Exception as e:
            print('error is: %s' % e)
        serializer.save(author=self.request.user, post=post)


class UserViewSet(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.save()
            return Response(serialize('json', [user, ]), status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
