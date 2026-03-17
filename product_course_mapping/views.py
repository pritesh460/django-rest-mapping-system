from rest_framework import generics
from .models import ProductCourseMapping
from .serializers import ProductCourseMappingSerializer

class ProductCourseListCreate(generics.ListCreateAPIView):
    queryset = ProductCourseMapping.objects.all()
    serializer_class = ProductCourseMappingSerializer

class ProductCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductCourseMapping.objects.all()
    serializer_class = ProductCourseMappingSerializer