from django.db import models
from django.contrib.auth import get_user_model
from group.models import Group

# Create your models here.
User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    objects = models.Manager()
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, related_name="group", blank=True, null=True)
    # поле для картинки
    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    def __str__(self):
        return self.text
