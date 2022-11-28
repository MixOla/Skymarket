from rest_framework import pagination, viewsets

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, CommentSerializer, AdCreateSerializer


class AdPagination(pagination.PageNumberPagination):
    pass


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.order_by('-created_at')
    default_serializer = AdSerializer
    serializer_class = AdSerializer
    serializer_classes = {
        "retrieve": AdSerializer,
        "create": AdCreateSerializer
    }

#
#     default_permission = [AllowAny()]
#     permissions = {
#         "create": [IsAuthenticated()],
#         "update": [IsAuthenticated(), IsOwnerAdOrStaff()],
#         "partial_update": [IsAuthenticated(), IsOwnerAdOrStaff()],
#         "destroy": [IsAuthenticated(), IsOwnerAdOrStaff()]
#     }
#
#     def get_permissions(self):
#         return self.permissions.get(self.action, self.default_permission)
#
    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)
#
#     def list(self, request, *args, **kwargs):
#         categories = request.GET.getlist('cat')
#         if categories:
#             self.queryset = self.queryset.filter(
#                 category_id__in=categories
#             )
#
#         text = request.GET.get('text')
#         if text:
#             self.queryset = self.queryset.filter(
#                 name__icontains=text)
#
#         location = request.GET.get('location')
#         if location:
#             self.queryset = self.queryset.filter(
#                 author__location__name__icontains=location
#             )
#
#         price_from = request.GET.get('price_from', None)
#         price_to = request.GET.get('price_to', None)
#         if price_to:
#             self.queryset = self.queryset.filter(price__lte=price_to)
#         if price_from:
#             self.queryset = self.queryset.filter(price__gte=price_from)
#
#         return super().list(self, request, *args, **kwargs)



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.order_by('-created_at')
    default_serializer = CommentSerializer
    serializer_class = CommentSerializer
    serializer_classes = {
        "retrieve": CommentSerializer,
        "create": CommentSerializer
    }