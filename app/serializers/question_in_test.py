from rest_framework import routers, viewsets, serializers, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from app.models import QuestionInTestModel,QuestionModel
from .question import QuestionSerializer


class QuestionInTestSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(
        read_only=True
    )

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(QuestionInTestSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = QuestionInTestModel
        fields = ('__all__')
    
    def create(self, validated_data):
        q = self.initial_data.pop(0)
        qit = QuestionModel.objects.get(id=q['question'])
        validated_data['question'] = qit
        return super().create(validated_data)

class QuestionInTestViewSet(viewsets.ModelViewSet):
    queryset = QuestionInTestModel.objects.all()
    serializer_class = QuestionInTestSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # self.user = request.user
        listOfQuestionsIT = request.data


        serializer = self.get_serializer(data=listOfQuestionsIT, many=True)
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED,
                            headers=headers)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_router_urls():
    router = routers.DefaultRouter()
    router.register('', QuestionInTestViewSet)
    # router.register('many/', buy_ticket)
    return router.urls