from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.forms.models import BaseModelFormSet, BaseInlineFormSet
from .models import *


class InspectionFormForm(forms.ModelForm):
    name = forms.CharField(validators=[MaxLengthValidator(100), MinLengthValidator(5)])

    class Meta:
        model = InspectionForm
        fields = ['name', 'is_verified']


class InspectionCategoryForm(forms.ModelForm):
    # category = forms.CharField(required=True, validators=[MaxLengthValidator(100), MinLengthValidator(5)])

    class Meta:
        model = Category
        fields = ['category']

    def __init__(self, *args, **kwargs):
        super(InspectionCategoryForm, self).__init__(*args,**kwargs)
        self.fields['category'].widget.attrs = {'class':'form-control'}
        # print('self.is_valid()', self.is_valid())
        # if not self.is_valid():
        #     self.fields['category'].widget.attrs = {'class': 'is-invalid'}


class QuestionForm(forms.ModelForm):
    question = forms.CharField(required=True, validators=[MaxLengthValidator(100), MinLengthValidator(5)])
    is_saved = forms.BooleanField()

    class Meta:
        model = Question
        fields = ['question', 'answer', 'option_type', 'answer_type', 'is_saved']

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args,**kwargs)
        self.fields['option_type'].widget.attrs = {'class':'form-control'}
        self.fields['answer_type'].widget.attrs = {'class':'form-control answer_type'}


class AnswerForm(forms.ModelForm):
    answer = forms.CharField(required=True, validators=[MaxLengthValidator(100), MinLengthValidator(5)])

    class Meta:
        model = Answer
        fields = ['answer', 'answer_priority', 'comment']

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args,**kwargs)
        self.fields['answer_priority'].widget.attrs = {'class':'form-control'}
        self.fields['comment'].widget.attrs = {'rows':'5'}


class BaseCategoryFormset(BaseInlineFormSet):

    def __init__(self, *args, **kwargs):
        super(BaseCategoryFormset, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False

    def add_fields(self, form, index):
        super(BaseCategoryFormset, self).add_fields(form, index)

        form.nested = question_formset(
            instance = form.instance,
            data=form.data if form.is_bound else None,
            prefix='%s-%s' % (
                form.prefix,
                question_formset.get_default_prefix()),
        )

    def is_valid(self):
        result = super(BaseCategoryFormset, self).is_valid()

        if self.is_bound:
            for form in self.forms:
                if hasattr(form, 'nested'):
                    result = result and form.nested.is_valid()
        return result

    def save(self, commit=True):
        result = super(BaseCategoryFormset, self).save(commit=commit)

        for form in self.forms:
            if hasattr(form, 'nested'):
                if not self._should_delete_form(form):
                    form.nested.save(commit=commit)

        return result


class BaseQuestionFormset(BaseInlineFormSet):

    def __init__(self, *args, **kwargs):
        super(BaseQuestionFormset, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False

    def add_fields(self, form, index):
        super(BaseQuestionFormset, self).add_fields(form, index)

        form.nested = answer_formset(
            instance = form.instance,
            data=form.data if form.is_bound else None,
            prefix='%s-%s' % (
                form.prefix,
                answer_formset.get_default_prefix()),
        )

    def is_valid(self):
        result = super(BaseQuestionFormset, self).is_valid()

        if self.is_bound:
            for form in self.forms:
                if hasattr(form, 'nested'):
                    result = result and form.nested.is_valid()
        return result

    def save(self, commit=True):
        result = super(BaseQuestionFormset, self).save(commit=commit)

        for form in self.forms:
            if hasattr(form, 'nested'):
                if not self._should_delete_form(form):
                    form.nested.save(commit=commit)

        return result


class BaseAnswerFormset(BaseInlineFormSet):

    def __init__(self, *args, **kwargs):
        super(BaseAnswerFormset, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.empty_permitted = False


answer_formset = forms.inlineformset_factory(Question,Answer,form=AnswerForm, formset=BaseAnswerFormset, extra=1, can_delete_extra=True, validate_max=True)

question_formset = forms.inlineformset_factory(InspectionCategory, Question, form=QuestionForm, formset=BaseQuestionFormset, extra=1, can_delete_extra=True, validate_max=True)

category_formset = forms.inlineformset_factory(InspectionForm, InspectionCategory, form=InspectionCategoryForm, formset=BaseCategoryFormset, extra=1, can_delete_extra=True, validate_max=True)


class GetAnswerFieldForm(forms.Form):
    answer = forms.CharField()

    # def __int__(self, *args, **kwargs):
    #     super(GetAnswerFieldForm, self).__init__(*args, **kwargs)
    #     pass