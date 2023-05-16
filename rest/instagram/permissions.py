from tkinter.tix import Tree
from rest_framework import permissions

class IsAuthorOrReadonly(permissions.BasePermission):
            #인증된 유저에 한해 목록조회/포스팅 등록 허용 
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        #  현재 method 안전한 요청이면 인증여부 상관없이 허용
        if request.method in permissions.SAFE_METHODS:
            return True 
        return obj.author == request.user