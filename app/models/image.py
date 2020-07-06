from django.db import models
from django.db.models import ImageField


class ImageModel(models.Model):
    file = ImageField(upload_to='media/')

    def __str__(self):
        return self.file.name
