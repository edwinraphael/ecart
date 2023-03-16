from ecart.models import Category,Products,Cart,Reviews
from rest_framework import serializers
from django.contrib.auth.models import User

class CategorySerialzer(serializers.ModelSerializer):
    is_active=serializers.CharField(read_only=True)
    class Meta:
        model=Category
        fields=["category_name","is_active"]

class ProductSerializer(serializers.ModelSerializer):
    category=serializers.CharField(read_only=True)
    class Meta:
        model=Products
        fields="__all__"

    def create(self, validated_data):
        category=self.context.get("category")
        return Products.objects.create(**validated_data,category=category)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","username","password","email"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class CartSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    product=ProductSerializer(read_only=True)
    created_date=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    class Meta:
        model=Cart
        fields="__all__"

    def create(self, validated_data):
        product = self.context.get("product")
        user=self.context.get("user")

        return Cart.objects.create(**validated_data,user=user,product=product)


class ReviewSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        fields="__all__"
    def create(self, validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Reviews.objects.create(**validated_data,user=user,product=product)