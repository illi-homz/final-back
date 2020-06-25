from rest_framework import routers, viewsets, serializers, permissions
from app.models import GroupQuestionsModel


class GroupQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupQuestionsModel
        fields = ('title', 'questions')

class GroupQuestionViewSet(viewsets.ModelViewSet):
    queryset = GroupQuestionsModel.objects.all()
    serializer_class = GroupQuestionSerializer
    # permission_classes = [permissions.IsAuthenticated]


def get_router_urls():
    router = routers.DefaultRouter()
    router.register('', GroupQuestionViewSet)
    return router.urls