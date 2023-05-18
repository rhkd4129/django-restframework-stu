from re import search
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from rest_framework import serializers
from .models import Post
from rest_framework import generics
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsAuthorOrReadonly
from rest_framework.filters import SearchFilter, OrderingFilter

# user. is_activce  is_staff is_superuser
# IsAuthenticatedOrReadOnly비인증요청에게는 읽기 권한만 허용
# class PublicPostListAPIView(generics.ListCreateAPIView)
#     queryset =Post.objects.filter(is_public = True)
#     serializer_class = PostSerializer

# class PublicPostListAPIView(APIView):
#     def get(self,request,format = None):
#         qs = Post.objects.filter(is_public = True)
#         serializer = PostSerializer(qs,many = True)
#         return Response(serializer.data)
# public_post_list = PublicPostListAPIView.as_view()


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadonly]  # 접근을위해서는 로그인이 되어있어야한다

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["messages"]
    # search_fields =['^=messages']
    # ordering=[]
    # 커스텀
    @action(detail=False, methods=["GET"])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        # serializer = PostSerializer(qs,many = True)
        return Response(serializer.data)

    @action(detail=True, methods=["PATCH"])  # detail 특정대상을 찍느냐  안찍느냐
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=["is_public"])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_create(self, serializer):  # serializer,save() 기본구현
        author = self.request.user
        ip = self.request.META["REMOTE_ADDR"]
        serializer.save(ip=ip, author=author)

    # 원래 list c,deso,,다 구현해야되는데 모덾viewset쓰면 다 지원
