from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post
from rest_framework.response import Response
from rest_framework.decorators import api_view



# class PublicPostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer



# class PublicPostListAPIView(APIView):
#     def get(self,reqeust):
#         qs = Post.objects.filter(is_public = True)
#         serializer = PostSerializer(qs,many = True)
#         return Response(serializer.data)
    
# public_post_list =PublicPostListAPIView.as_view()


@api_view(['GET'])
def public_post_list(request):
    qs = Post.objects.filter(is_public = True)
    serializer = PostSerializer(qs,many = True)
    return Response(serializer.data)



class PostViewSet(ModelViewSet):
    queryset =Post.objects.all()
    serializer_class = PostSerializer

    def dispatch(self, request, *args, **kwargs): #실제 요청이 올떄마다 요청되는 함수?
        print(request.body)#logger
        print(request.POST)#logger
        return super().dispatch(request, *args, **kwargs)
    
