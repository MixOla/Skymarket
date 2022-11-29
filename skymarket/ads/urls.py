from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet

ads_router = SimpleRouter()

# регистрируем ViewSet, который импортирован из приложения Djoser
ads_router.register("ads", AdViewSet, basename="ads")
# users_router.register("users", UserViewSet, basename="users")
urlpatterns = [
    path("", include(ads_router.urls)),
]
