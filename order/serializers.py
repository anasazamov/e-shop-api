from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Order, Comment, Like

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class Orderserializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    user = Userserializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = '__all__'
class Commentserializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    user = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = '__all__'
class Likeserializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)
    user = ProductSerializer(many=True, read_only=True)
    class Meta:
        fields = '__all__'