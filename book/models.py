from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=225)
    image = models.ImageField(
        default="Python.png", upload_to="category_images", null=True, blank=True
    )

    def __str__(self):
        return self.name


class Question(models.Model):
    # question = models.CharField(max_length=225)
    question = RichTextField(null=True, blank=True)
    category = models.ForeignKey(
        Category, related_name="question_category", on_delete=models.CASCADE
    )
    # answer = models.TextField()
    answer = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.question
