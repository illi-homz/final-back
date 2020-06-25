from django.db import models
from django.db.models import CharField, ForeignKey, ManyToManyField
from . import QuestionModel


class GroupQuestionsModel(models.Model):
    title = CharField(max_length=30)
    questions = ManyToManyField(QuestionModel)

    # class Meta:
    #     ordering = ['title']

    def __str__(self):
        return self.title
