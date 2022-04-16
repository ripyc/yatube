from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Group(models.Model):
    tittle = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.tittle
