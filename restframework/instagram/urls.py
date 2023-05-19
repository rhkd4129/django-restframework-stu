
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views



router = DefaultRouter()
router.register("post", views.PostViewSet) #2개의ㅏ url만들어준다 
# url patterns List

urlpatterns = [
    # path('public/',views.PublicPostListAPIView.as_view()),
    path('public/',views.public_post_list),
    path('',include(router.urls)),
]

