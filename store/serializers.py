from rest_framework import serializers
from store.models import Category,Products
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True) 

    class Meta:
        model=User
        fields=["id","username","email","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class CategorySerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)


    class Meta:
        model=Category
        fields="__all__"


class productserializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    category=serializers.CharField(read_only=True)

    class Meta:
        model=Products
        fields="__all__"


