from django.db import models
from django.db.models import CharField, IntegerField, DateField, TextField
from django.db.models import ManyToManyField, ForeignKey
from app.models.question_in_test import QuestionInTestModel
from . import MyUser


class TestModel(models.Model):
    title = CharField(max_length=30)
    about = TextField(blank=True, null=True)
    start_date = DateField()
    end_date = DateField()
    time_on_question = IntegerField()
    questions = ManyToManyField(QuestionInTestModel)
    tested_users = ManyToManyField(MyUser)

    def __str__(self):
        return self.title


