from rest_framework import routers, viewsets, serializers, permissions, status
from rest_framework.response import Response
from app.models import TestModel, QuestionInTestModel, MyUser
from .user import UserSerializer
from .question_in_test import QuestionInTestSerializer


class TestSerializer(serializers.ModelSerializer):
    tested_users = UserSerializer(many=True, read_only=True)
    questions = QuestionInTestSerializer(many=True, read_only=True)

    class Meta:
        model = TestModel
        fields = ('__all__')
    
    def validate(self, attrs):
        questionsIT_list = self.initial_data['questions']
        users = self.initial_data['tested_users']
        attrs['questions'] = []
        attrs['tested_users'] = []
        for q in self.initial_data['questions']:
            qit = QuestionInTestModel.objects.get(id=q)
            attrs['questions'].append(qit)
        for u in self.initial_data['tested_users']:
            user = MyUser.objects.get(id=u)
            attrs['tested_users'].append(user)
        return super().validate(attrs)


class TestViewSet(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer
    # permission_classes = [permissions.IsAuthenticated]


def get_router_urls():
    router = routers.DefaultRouter()
    router.register('', TestViewSet)
    return router.urls