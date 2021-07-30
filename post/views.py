from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import PostSerializer
from rest_framework.generics import(CreateAPIView,ListAPIView,RetrieveUpdateDestroyAPIView)
from .models import Post
from .permissions import IsOwner
from account.models import UserAccount
from account.serializers import UserCreateSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend




class PostListView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city', 'size']


class PostCreateView(CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated,IsOwner]


@api_view(['GET'])
def postAuthor(request, pk):
    author = UserAccount.objects.get(id=pk)
    serializer = UserCreateSerializer(author, many=False)
    return Response(serializer.data)






