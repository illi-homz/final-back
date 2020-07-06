# from django.contrib.auth.models import User
from app.models import MyUser
from rest_framework import routers, serializers, viewsets, permissions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        # fields = ('id', 'username', 'first_name', 'last_name', 'email')
        fields = ('__all__')
        extra_kwargs = {'password': {'write_only': True}}

class UserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


def get_router_urls():
    router = routers.DefaultRouter()
    router.register('', UserViewSet)
    return router.urls