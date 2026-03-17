from django.urls import path
from .views import VendorProductListCreate, VendorProductDetail

urlpatterns = [
    path('', VendorProductListCreate.as_view()),
    path('<int:pk>/', VendorProductDetail.as_view()),
]