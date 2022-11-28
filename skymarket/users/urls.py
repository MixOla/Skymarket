from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from django.urls import path

users_router = SimpleRouter()

# регистрируем ViewSet, который импортирован из приложения Djoser
users_router.register("users", UserViewSet, basename="users")
# users_router.register("users", UserViewSet, basename="users")
urlpatterns = [
    path("", include(users_router.urls)),
]
