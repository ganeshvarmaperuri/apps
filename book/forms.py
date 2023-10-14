from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "image"]


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
