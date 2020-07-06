from rest_framework import routers, viewsets, serializers, permissions, status
from rest_framework.response import Response
from app.models import ResultModel, MyUser
from .test import TestSerializer, TestModel, UserSerializer

class ResultSerializer(serializers.ModelSerializer):
    test = TestSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = ResultModel
        fields = ('__all__')
    
    def create(self, validated_data):
        init_data = self.initial_data
        test = TestModel.objects.get(id=init_data['test'])
        user = MyUser.objects.get(id=init_data['user'])
        validated_data['test'] = test
        validated_data['user'] = user
        return super().create(validated_data)

class ResultViewSet(viewsets.ModelViewSet):
    queryset = ResultModel.objects.all()
    serializer_class = ResultSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        if (self.request.query_params):
            userID = self.request.query_params['user']
            queryset = queryset.filter(user__id=userID)
            return queryset
        return queryset


def get_router_urls():
    router = routers.DefaultRouter()
    router.register('', ResultViewSet)
    return router.urls