from django import forms
from .models import Name

'''
To save the user input into the DB
'''
class UserForm(forms.ModelForm):
    class Meta:
        model = Name  #inline class..name model should be there
        fields =  "__all__"  #to include all the columns.....take all the fields from the model and place them into the form
    # exclude = ['field1',2] to exclude field
    # fields = ('fields1',)
