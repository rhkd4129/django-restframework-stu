from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('apt-token-auth',obtain_auth_token),
]