from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Category, Question
from .forms import *


class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "book/create_category.html"
    success_url = reverse_lazy("list_category")


class CategoryList(ListView):
    model = Category
    template_name = "book/list_category.html"
    context_object_name = "categories"


class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "book/update_category.html"
    success_url = reverse_lazy("list_category")


class CategoryDetail(DetailView):
    model = Category
    template_name = "book/details_category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        questions = Question.objects.filter(category__id=self.kwargs["pk"])
        context["questions"] = questions
        context["category"] = Category.objects.get(id=self.kwargs["pk"])
        return context


class QuestionCreate(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = "book/create_question.html"
    success_url = reverse_lazy("create_question")


class QuestionUpdate(UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = "book/update_question.html"
    success_url = reverse_lazy("list_category")

    def get_success_url(self):
        question = Question.objects.get(id=self.kwargs["pk"])
        return reverse_lazy("details_category", kwargs={"pk": question.category.id})


# class QuestionList(ListView):
#     model = Question
#     template_name = 'book/list_question.html'
#     content_type = 'questions'
#
#     def get_queryset(self):
#         return super(QuestionList, self).get_queryset().filter(
#             category_id=self.kwargs['pk']
#         )
#
