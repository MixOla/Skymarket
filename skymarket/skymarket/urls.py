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
router.register('user', UserViewSet)
router.register('ad', AdViewSet)
router.register('comment', CommentViewSet)


urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    # path('api-auth', include('rest_framework.urls')),
    path('api/', include('users.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
