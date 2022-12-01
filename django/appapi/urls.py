from django.urls import path, include
from .api import UserBottleViewSet, UserViewSet, RasPiViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'userbottle', UserBottleViewSet)
router.register(r'user', UserViewSet)
router.register(r'raspiinformation', RasPiViewSet)

urlpatterns = [
    path('', include(router.urls)),
]