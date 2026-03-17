from django.urls import path
from .views import ProductCourseListCreate, ProductCourseDetail

urlpatterns = [
    path('', ProductCourseListCreate.as_view()),
    path('<int:pk>/', ProductCourseDetail.as_view()),
]