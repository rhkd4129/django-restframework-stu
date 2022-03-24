from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from rest_framework import serializers
from .models import Post
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

# class PublicPostListAPIView(generics.ListCreateAPIView)
#     queryset =Post.objects.filter(is_public = True)   
#     serializer_class = PostSerializer

# class PublicPostListAPIView(APIView):
#     def get(self,request,format = None):
#         qs = Post.objects.filter(is_public = True)
#         serializer = PostSerializer(qs,many = True)
#         return Response(serializer.data)    
# public_post_list = PublicPostListAPIView.as_view()

@api_view(['GET'])
def public_post_list(request):
     qs = Post.objects.filter(is_public = True)
     serializer = PostSerializer(qs,many = True)
     return Response(serializer.data)

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer




# APIView - mixinis -generics - viewset
# APIView
# DRF의 2가지 기본뷰
# APIView :클래스 기반 뷰  (django에서 기본view를 상속받는것과 같은) -> Generic - > viewset
# 하나의 CBV이므로 하나의 URL처리만 가능    iewset제외(2개의 url처리)
# 각 method(g,p,p,d)에 맞게 멤버함수를 구현하면 해당 method 요청시 호출
# 직/비렬화 json등 인증체크,사용자 제한체크,권한클래스 지정,요청된 api 버전 문자열을 탐지하여  request.version에저장
# inintal에서 다 선언함

# @api_view : 함수 기반 뷰를 위한 장식자

# @csrf_exempt면제되는
# def post_list(request):
#     pass
# post_list = csrf_exempt(post_list)  리액트 = 고차 컴포넌트

# generics.CreateAPIView  + generics.ListAPIView   = generics.ListCreateAPIView
# generics.DestroyAPIView....  많다 


# DRF에서 지원하는 믹스인
# CRATE,List,Retrieve,Update,Destroy(mode)Mixin
# retrieve 되찾아오다[회수하다] (=recover) (정보를) 검색하다 수습[개선]하다, (잃은 것을) 되찾다
# exempt면제되는

# pyton mro mixin을앞에