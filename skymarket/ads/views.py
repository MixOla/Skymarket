from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, CommentSerializer, AdCreateSerializer, AdDetailSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 3


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.order_by('-created_at')
    pagination_class = AdPagination
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['retrieve', ]:
            return AdDetailSerializer
        else:
            return AdSerializer

    @action(detail=False)
    def me(self, request, *args, **kwargs):
        self.queryset = Ad.objects.filter(author=request.user)
        return super().list(self, self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.order_by('-created_at')
    default_serializer = CommentSerializer
    serializer_class = CommentSerializer
    serializer_classes = {
        "retrieve": CommentSerializer,
        "create": CommentSerializer
    }
