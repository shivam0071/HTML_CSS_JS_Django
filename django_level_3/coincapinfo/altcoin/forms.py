from django import forms
from .models import BasicInfo,deepInfo

'''
To save the user input into the DB
'''
class BasicInfoForm(forms.ModelForm):
    class Meta:
        model = BasicInfo  #inline class..name model should be there
        fields =  "__all__"  #to include all the columns.....take all the fields from the model and place them into the form
    # exclude = ['field1',2] to exclude field
    # fields = ('fields1',)

class DeepInfoForm(forms.ModelForm):
    class Meta:
        model = deepInfo  #inline class..name model should be there
        fields =  "__all__"  #to include all the columns.....take all the fields from the model and place them into the form
