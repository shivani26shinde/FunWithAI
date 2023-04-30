from django import forms

class JobSearchForm(forms.Form):
    position = forms.CharField()
    location = forms.CharField()
    company = forms.CharField()