from django.db import models
from django.db.models import CharField, TextField


class QuestionModel(models.Model):
    qtype = CharField(max_length=20)
    question = TextField()
    answer = TextField(blank=True)
    variants = TextField(blank=True)
    img = TextField(blank=True)

    class Meta:
        ordering = ['question']

    def __str__(self):
        return self.question