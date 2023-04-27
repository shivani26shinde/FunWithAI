from django import forms

class FoodForm(forms.Form):
    food = forms.CharField(max_length=200, label='What did you eat?')
    amount = forms.IntegerField(label='How much did you eat? (in grams)')
