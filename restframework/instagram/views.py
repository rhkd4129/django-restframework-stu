from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post
from rest_framework.response import Response
from rest_framework.decorators import api_view,action



# class PublicPostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer



# class PublicPostListAPIView(APIView):
#     def get(self,reqeust):
#         qs = Post.objects.filter(is_public = True)
#         serializer = PostSerializer(qs,many = True)
#         return Response(serializer.data)
    
# public_post_list =PublicPostListAPIView.as_view()


# @api_view(['GET'])
# def public_post_list(request):
#     qs = Post.objects.filter(is_public = True)
#     serializer = PostSerializer(qs,many = True)
#     return Response(serializer.data)


from rest_framework.permissions import IsAuthenticated
class PostViewSet(ModelViewSet):
    queryset =Post.objects.all()
    serializer_class = PostSerializer
    # authentication_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        # FIXME: 인증이 되었다는 가정하에 
        author = self.request.user
        ip = self.request.META['REMOTE_ADDR']
        serializer.save(ip = ip,author =author)
       

    @action(detail=False,methods=['GET'])
    def public(self,request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs,many = True)
        return Response(serializer.data)
    
    @action(detail=False,methods=['PATCH'])
    def set_public(self,request,pk):
        instance = self.get_object()
        instance.is_public =True
        instance.save(update_fields =['is_public'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
     
    
    # def dispatch(self, request, *args, **kwargs): #실제 요청이 올떄마다 요청되는 함수?
    #     print(request.body)#logger
    #     print(request.POST)#logger
    #     return super().dispatch(request, *args, **kwargs)
    
