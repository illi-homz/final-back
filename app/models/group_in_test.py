from django.db import models
from django.db.models import ForeignKey, IntegerField
from . import GroupQuestionsModel


class GroupInTestModel(models.Model):
    group = ForeignKey(GroupQuestionsModel, models.SET_NULL, blank=True, null=True)
    price = IntegerField()

    # def __str__(self):
    #     return f'{self.group.title[:10]}... - на {self.price}'
