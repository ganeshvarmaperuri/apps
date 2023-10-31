from django.db import models
from django.contrib.auth.models import User

AnswerType = (
        ("Radio", "Radio"),
        ("Checkbox", "Checkbox"),
        ("Input", "Input"),
        ("Dropdown", "Dropdown"),
    )

AnswerPriority = (
    ("Action", "Action"),
    ("Monitor", "Monitor"),
    ("Normal", "Normal"),
    ("N/A", "N/A"),
)


class OptionTitle(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'


class Option(models.Model):
    label = models.CharField(max_length=50)
    title = models.ForeignKey(OptionTitle, related_name='option_title', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}-{self.label}'


class InspectionForm(models.Model):
    name= models.CharField(max_length=100)
    is_verified= models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.category


class InspectionCategory(models.Model):
    category = models.ForeignKey(Category, related_name='inspection_category', on_delete=models.CASCADE, null=False, blank=False)
    inspection_form = models.ForeignKey(InspectionForm, related_name='inspection_form_category',
                                        on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.category} in {self.inspection_form}'


class Question(models.Model):
    question = models.CharField(max_length=225, null=True,blank=True)
    category = models.ForeignKey(InspectionCategory, on_delete=models.SET_NULL, related_name='inspection_category_question', null=True, blank=True)
    answer = models.CharField(max_length=100, null=True, blank=True)
    option_type = models.ForeignKey(OptionTitle, related_name='question_options', on_delete=models.SET_NULL, null=True, blank=True)
    answer_type = models.CharField(max_length=30, choices=AnswerType, null=True, blank=True)
    answer_priority = models.CharField(choices=AnswerPriority, default='N/A', max_length=50, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    is_saved = models.BooleanField(default=False, null=True,blank=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="question_answer", on_delete=models.CASCADE, null=False, blank=False)
    answer = models.CharField(max_length=300, null=True, blank=True)
    answer_priority = models.CharField(choices=AnswerPriority, default='Normal', max_length=50, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.question}-{self.answer}'
