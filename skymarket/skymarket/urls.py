import users
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from djoser.views import UserViewSet
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework import routers


router = routers.SimpleRouter()
router.register('user', UserViewSet)


urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    path('user/', include('users.urls'))
]
urlpatterns += router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
