from atexit import register
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post',views.PostViewSet)
# url patterns List

urlpatterns =[
   # path('public/',views.public_post_list),
   path('',include(router.urls)),
    
]

