from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# ModelViewSet
# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# ReadOnlyModelViewSet
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDummyApiView(APIView):
    def get(self, request, format=None):
        return Response({"name": "DUMMY!"})


@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)