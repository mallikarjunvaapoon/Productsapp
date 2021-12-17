import time
from .models import Brands, Product
from .serializers import BrandSerializer, ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser



class BrandView(APIView):
  def get(self, request):
    brand = Brands.objects.all()
    serializer = BrandSerializer(brand, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = BrandSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)

class ProductView(APIView):
  def get(self, request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


  parser_classes = (MultiPartParser, FormParser, FileUploadParser)
  def post(self, request):
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    time.sleep(120)
    return Response(serializer.data)

