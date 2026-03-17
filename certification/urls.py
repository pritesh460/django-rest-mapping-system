from django.urls import path
from .views import CertificationListCreate, CertificationDetail

urlpatterns = [
    path('certifications/', CertificationListCreate.as_view()),
    path('certifications/<int:pk>/', CertificationDetail.as_view()),
]