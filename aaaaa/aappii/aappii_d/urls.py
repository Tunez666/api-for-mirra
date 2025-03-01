from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArrrViewSet

router = DefaultRouter()
router.register(r'arrr', ArrrViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get_data/', ArrrViewSet.as_view({'get': 'get_data'})),
    path('write_data/', ArrrViewSet.as_view({'post': 'write_data'})),
]