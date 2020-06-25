from django.db import models
from django.db.models import ForeignKey, IntegerField
from . import QuestionModel


class QuestionInTestModel(models.Model):
    question = ForeignKey(QuestionModel, models.SET_NULL, blank=True, null=True)
    price = IntegerField()

    def __str__(self):
        return f'{self.question.question[:10]}... - на {self.price}'
