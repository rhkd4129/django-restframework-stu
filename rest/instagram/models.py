from django.db import models
from django.conf import settings


# db_index 속성은 인덱싱이 가능하게끔 해주는 것이며 True 값을 준다 ( 이름으로도 검색할수있도록 )
# allow_unicode에 True 값을 줘야 한국어로 작성을 할수있다


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    messages = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False, db_index=True)
    ip = models.GenericIPAddressField(null=True, editable=False)
