from django import forms
from .models import AccountModel


class AccountForm(forms.Form):
    # project_name = forms.ChoiceField(choices=('Проект1','Проект2'))
    project_name = forms.CharField(max_length=256, required=False)
    # date_start = forms.DateField(input_formats=None)
    # date_end = forms.DateField(input_formats=None)