from django import forms
from .models import *


class EmployeeSearchForm(forms.ModelForm):

    export_to_CSV = forms.BooleanField(required=False)
    name=forms.CharField(required=False)
    class Meta:

        model = Employee
        fields = ['name']