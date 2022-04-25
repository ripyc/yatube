from django.forms import ModelForm, Textarea
from .models import Group, Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["text", "group"]

        widgets = {
            "text": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Текст записи дневника"
            })

        }
