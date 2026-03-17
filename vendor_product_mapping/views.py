from rest_framework import generics
from .models import VendorProductMapping
from .serializers import VendorProductMappingSerializer

class VendorProductListCreate(generics.ListCreateAPIView):
    queryset = VendorProductMapping.objects.all()
    serializer_class = VendorProductMappingSerializer

class VendorProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VendorProductMapping.objects.all()
    serializer_class = VendorProductMappingSerializer