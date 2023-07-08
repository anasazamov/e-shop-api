from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Product, Order, Comment, Like, User
from .serializers import ProductSerializer

# Create your views here.

class ProductView(APIView):
    def get(self, request: Request, pk=None) -> Response:
        if pk is None:
            product = Product.objects.all()
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)