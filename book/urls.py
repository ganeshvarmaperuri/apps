from django.urls import path
from .views import *

urlpatterns = [
    path("create-category/", CategoryCreate.as_view(), name="create_category"),
    path("list-category/", CategoryList.as_view(), name="list_category"),
    path("update-category/<slug:pk>", CategoryUpdate.as_view(), name="update_category"),
    path(
        "category/details/<slug:pk>", CategoryDetail.as_view(), name="details_category"
    ),
    path("question/create/", QuestionCreate.as_view(), name="create_question"),
    path("question/update/<slug:pk>", QuestionUpdate.as_view(), name="update_question"),
    # path('question/update/<slug:pk>', CategoryUpdate.as_view(), name='update_question'),
]
