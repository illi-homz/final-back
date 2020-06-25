from django.db import models
from django.db.models import TextField, ForeignKey, DateTimeField
from app.models.test import TestModel
from . import MyUser


class ResultModel(models.Model):
    test = ForeignKey(TestModel, models.SET_NULL, blank=True, null=True)
    user = ForeignKey(MyUser, models.CASCADE, blank=True, null=True)
    answers = TextField()
    create_date = DateTimeField(auto_now=True)

    # def __str__(self):
    #     return f'{self.user.username} - Тест: {self.test.title}'