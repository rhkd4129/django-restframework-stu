from .models import Post
from rest_framework import serializers
from django.contrib.auth import get_user_model


class PostSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(
        source="author.username"
    )  # 모델 필드에는 없어서 임의로 만든다
    author_email = serializers.ReadOnlyField(source="author.email")
    # username = AuthorSerializer()                                          #author.email 작성자 이메일

    class Meta:
        model = Post
        fields = [
            "pk",
            "username",  # 만든 필드
            "messages",
            "author_email",
            "created_at",
            "updated_at",
            "is_public",
            "ip",
        ]


class AuthorSerializer(serializers.ModelSerializer):
    # 아니면 중첩된 serializer를 별도로 만ㄷ르어서 적용할수도잇따
    class Meta:
        model = get_user_model()
        fields = ["username", "email"]


# form생성자의 첫번째 인자는 data이지만
# Serializer 생성자의 첫번쨰는 인자는 instance !!
