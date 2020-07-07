from rest_framework import routers, viewsets, serializers, permissions, status
from rest_framework.response import Response
# from rest_framework import 
from app.models import TestModel
from .user import UserSerializer, MyUser
from .question_in_test import QuestionInTestSerializer, QuestionInTestModel
from .group_in_test import GroupInTestSerializer, GroupInTestModel


class TestSerializer(serializers.ModelSerializer):
    tested_users = UserSerializer(many=True, read_only=True)
    questions = QuestionInTestSerializer(many=True, read_only=True)
    groups = GroupInTestSerializer(many=True, read_only=True)

    class Meta:
        model = TestModel
        fields = ('__all__')
    
    def validate(self, attrs):
        attrs['questions'] = []
        attrs['tested_users'] = []
        attrs['groups'] = []
        for u in self.initial_data['tested_users']:
            user = MyUser.objects.get(id=u)
            attrs['tested_users'].append(user)
        try:
            if self.initial_data['questions']:
                for q in self.initial_data['questions']:
                    qit = QuestionInTestModel.objects.get(id=q)
                    attrs['questions'].append(qit)
        except:
            pass
        try:
            if self.initial_data['groups']:
                for g in self.initial_data['groups']:
                    group = GroupInTestModel.objects.get(id=g)
                    attrs['groups'].append(group)
        except:
            pass
        return super().validate(attrs)


class TestViewSet(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        if (self.request.query_params):
            userID = self.request.query_params['user']
            queryset = queryset.filter(tested_users__id=userID)
            return queryset
        return queryset


def get_router_urls():
    router = routers.DefaultRouter()
    router.register('', TestViewSet)
    return router.urls