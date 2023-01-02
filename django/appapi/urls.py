from django.urls import path, include
from .api import UserBottleViewSet, UserViewSet, RasPiViewSet
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'userbottle', UserBottleViewSet)
router.register(r'user', UserViewSet)
router.register(r'raspiinformation', RasPiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('raspi/create', views.create, name='raspi_create'),
    path('raspi/index', views.index, name='raspi_index'),
    path('raspi/store', views.store, name='raspi_store'),
]