from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, reverse
from django.views.generic import View, CreateView, ListView, UpdateView

from .models import *
from .forms import *


def template(request):
    return render(request, "templates/base.html", {})


def form_repeater(request):
    return render(request, "templates/form_repeater/form_repeater.html", {})


class InspectionFormList(ListView):
    model = InspectionForm
    template_name = "form_repeater/list.html"
    context_object_name = "inspection_forms"


class CreateInspectionForm(View):
    template_name = "form_repeater/form_repeater1.html"

    def get(self, request):
        inspection_form = InspectionFormForm()
        formset = category_formset(
            prefix="category",
        )

        context = {"inspection_form": inspection_form, "formset": formset}
        return render(request, self.template_name, context)

    def post(self, request):
        inspection_form = InspectionFormForm(request.POST)
        formset = category_formset(request.POST, prefix="category")
        context = {"inspection_form": inspection_form, "formset": formset}
        if inspection_form.is_valid():
            instance = inspection_form.save(commit=False)
            instance.save()
            formset = category_formset(
                request.POST, prefix="category", instance=instance
            )
            if formset.is_valid():
                formset.save()
            else:
                return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, context)

        return redirect("inspection_forms_list")


class UpdateInspectionForm(View):
    # model = InspectionForm
    # form_class = InspectionFormForm
    template_name = "form_repeater/form_repeater1.html"

    def get(self, request, *args, **kwargs):
        get_form = InspectionForm.objects.get(id=self.kwargs["pk"])
        inspection_form = InspectionFormForm(instance=get_form)
        formset = category_formset(prefix="category", instance=get_form)

        context = {"inspection_form": inspection_form, "formset": formset}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        get_form = InspectionForm.objects.get(id=self.kwargs["pk"])
        inspection_form = InspectionFormForm(request.POST, instance=get_form)
        formset = category_formset(request.POST, prefix="category", instance=get_form)
        context = {"inspection_form": inspection_form, "formset": formset}
        if inspection_form.is_valid() and formset.is_valid():
            instance = inspection_form.save(commit=False)
            instance.save()
            formset = category_formset(
                request.POST, prefix="category", instance=instance
            )
            formset.save()

        else:
            return render(request, self.template_name, context)

        return redirect("inspection_forms_list")


def get_options(request):
    options = (
        OptionTitle.objects.get(id=request.GET.get("option_type"))
        .option_title.all()
        .values("label")
    )
    data = {
        "options": list(options),
    }
    return JsonResponse(data)
