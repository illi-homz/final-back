from rest_framework import routers, viewsets, serializers, permissions
from app.models import GroupQuestionsModel
from .question import QuestionSerializer, QuestionModel


class GroupQuestionSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = GroupQuestionsModel
        fields = ('__all__')
    
    def validate(self, attrs):
        questions = self.initial_data['questions']
        attrs['questions'] = []
        for q in questions:
            question = QuestionModel.objects.get(id=q)
            attrs['questions'].append(question)
        return super().validate(attrs)

class GroupQuestionViewSet(viewsets.ModelViewSet):
    queryset = GroupQuestionsModel.objects.all()
    serializer_class = GroupQuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


def get_router_urls():
    router = routers.DefaultRouter()
    router.register('', GroupQuestionViewSet)
    return router.urls