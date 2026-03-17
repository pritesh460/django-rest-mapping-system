from rest_framework import generics
from .models import CourseCertificationMapping
from .serializers import CourseCertificationMappingSerializer

class CourseCertificationListCreate(generics.ListCreateAPIView):
    queryset = CourseCertificationMapping.objects.all()
    serializer_class = CourseCertificationMappingSerializer

class CourseCertificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseCertificationMapping.objects.all()
    serializer_class = CourseCertificationMappingSerializer