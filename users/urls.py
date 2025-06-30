from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView
from .apps import UsersConfig
from .views import PaymentViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'payments', PaymentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/',UserCreateAPIView.as_view(), name= 'register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("list/", UserListAPIView.as_view(), name="users_list"),
    path("view/<int:pk>/", UserRetrieveAPIView.as_view(), name="users_detail"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="users_update"),
    path("delete/<int:pk>/", UserDestroyAPIView.as_view(), name="users_delete"),
]
urlpatterns += router.urls


