from django.urls import path
from .views import *

urlpatterns = [
    path("", template, name="template"),
    path("form_repeater", CreateInspectionForm.as_view(), name="form_repeater"),
    path("list/inspection_form", InspectionFormList.as_view(), name="inspection_forms_list"),
    path("update/<slug:pk>/inspection_form", UpdateInspectionForm.as_view(), name="inspection_forms_update"),
    path("get_options", get_options, name="get_options"),
]
