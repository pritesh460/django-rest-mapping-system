from django.urls import path
from .views import CourseCertificationListCreate, CourseCertificationDetail

urlpatterns = [
    path('', CourseCertificationListCreate.as_view()),
    path('<int:pk>/', CourseCertificationDetail.as_view()),
]