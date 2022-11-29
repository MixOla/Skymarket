import users
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from djoser.views import UserViewSet
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from ads.views import AdViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register('users', UserViewSet)
router.register('ads', AdViewSet)
router.register('comments', CommentViewSet)


urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    path('api/', include('users.urls')),
    path('api/', include('ads.urls')),


]
urlpatterns += router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
