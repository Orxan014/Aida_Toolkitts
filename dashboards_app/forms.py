from django.forms import ModelForm
from .models import Calendar


class PostForm(ModelForm):
    class Meta:
        model = Calendar
        fields = ['post_image']