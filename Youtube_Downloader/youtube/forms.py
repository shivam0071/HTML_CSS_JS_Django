from django import forms



class Youform(forms.Form):
    # name = forms.CharField(validators=[check_for_s]) #for above check
    url = forms.CharField(label='URL',widget=forms.TextInput(attrs={'placeholder': 'Enter URL here'})) #to get the html style text area
