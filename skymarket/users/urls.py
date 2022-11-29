from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

users_router = SimpleRouter()

# регистрируем ViewSet, который импортирован из приложения Djoser
users_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(users_router.urls)),
    path("token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("refresh/", TokenRefreshView.as_view(), name='token_refresh'),
]
