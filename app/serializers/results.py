from rest_framework import routers, viewsets, serializers, permissions, status
from app.models import ResultModel
from .test import TestSerializer, TestModel

class ResultSerializer(serializers.ModelSerializer):
    test = TestSerializer(read_only=True)
    class Meta:
        model = ResultModel
        fields = ('__all__')
    
    def create(self, validated_data):
        t = self.initial_data
        test = TestModel.objects.get(id=t['test'])
        validated_data['test'] = test
        return super().create(validated_data)

class ResultViewSet(viewsets.ModelViewSet):
    queryset = ResultModel.objects.all()
    serializer_class = ResultSerializer


def get_router_urls():
    router = routers.DefaultRouter()
    router.register('', ResultViewSet)
    return router.urls