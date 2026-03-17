from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

#  Swagger imports
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#  Home API
def home(request):
    return HttpResponse("API is running 🚀")

#  Swagger setup
schema_view = get_schema_view(
    openapi.Info(
        title="Core Project API",
        default_version='v1',
        description="API documentation for Vendor, Product, Course, Certification Mapping",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

#  URL Patterns
urlpatterns = [
    path('', home),

    path('admin/', admin.site.urls),

    #  Your APIs
    path('api/vendor-product/', include('vendor_product_mapping.urls')),
    path('api/product-course/', include('product_course_mapping.urls')),
    path('api/course-certification/', include('course_certification_mapping.urls')),

    #  Swagger URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
]