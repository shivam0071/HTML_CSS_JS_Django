from django import forms
from . import views

CHOICES = (('1', 'First',), ('2', 'Second',))
class Radioform(forms.Form):
    print('Inside farm',CHOICES)
    name = forms.CharField()
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
