# from django.contrib.auth.models import User
from app.models import MyUser
from rest_framework import routers, serializers, viewsets, permissions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email')
        extra_kwargs = {'password': {'write_only': True}}

class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAccountAdminOrReadOnly]


def get_router_urls():
    router = routers.DefaultRouter()
    router.register('', UserViewSet)
    return router.urls