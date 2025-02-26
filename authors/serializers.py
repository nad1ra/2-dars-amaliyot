from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.Serializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email', 'bio']


    def validate_email(self, value):
        if "@" not in value or not value.endswith("@gmail.com"):
            raise serializers.ValidationError("Noto‘g‘ri email formati! Faqat @ yoki gmail.com ham yozing.")
        return value


