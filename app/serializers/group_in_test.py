from rest_framework import routers, viewsets, serializers, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from app.models import GroupInTestModel, GroupQuestionsModel
from .group_questions import GroupQuestionSerializer


class GroupInTestSerializer(serializers.ModelSerializer):
    group = GroupQuestionSerializer(
        read_only=True
    )

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(GroupInTestSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = GroupInTestModel
        fields = ('__all__')
    
    def create(self, validated_data):
        g = self.initial_data.pop(0)
        git = GroupQuestionsModel.objects.get(id=g['group'])
        validated_data['group'] = git
        return super().create(validated_data)

class GroupInTestViewSet(viewsets.ModelViewSet):
    queryset = GroupInTestModel.objects.all()
    serializer_class = GroupInTestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # self.user = request.user
        listOfGroupsIT = request.data


        serializer = self.get_serializer(data=listOfGroupsIT, many=True)
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED,
                            headers=headers)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_router_urls():
    router = routers.DefaultRouter()
    router.register('', GroupInTestViewSet)
    return router.urls