from rest_framework import routers, viewsets, serializers, permissions
from app.models import ImageModel


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ('id', 'file')

class ImagesViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer
    # permission_classes = [permissions.IsAuthenticated]


def get_router_urls():
    router = routers.DefaultRouter()
    router.register('', ImagesViewSet)
    return router.urls