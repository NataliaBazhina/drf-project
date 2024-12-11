from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apps import UsersConfig
from .views import PaymentViewSet


router = DefaultRouter()
router.register(r'payments', PaymentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
urlpatterns += router.urls