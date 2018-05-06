from django import forms
from django.core import validators


# def check_for_s(value):  #value tells django we are looking for a value
#     if value[0].lower() != 's':
#         raise forms.ValidationError('Check out that S,Name should start with S :)')


class FormName(forms.Form):
    # name = forms.CharField(validators=[check_for_s]) #for above check
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea) #to get the html style text area

    # bot_catcher = forms.CharField(required=False, widget = forms.HiddenInput)
    # #How bot catcher works
    # def clean_botCatcher(self):
    #     bot_catcher = self.cleaned_data['bot_catcher']
    #     if len(bot_catcher) > 0:
    #         raise forms.ValidationError("Hey Botter!!")
    #     return bot_catcher

    #what we actually do

    # bot_catcher = forms.CharField(required=False, widget = forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    #now if we want to check for a particular value in any field such as text area or email
    # this is how it works...Make a function outside this class


    #now if we want to comfirm something...such as email entered or the password we can do so by:-
    verify_email = forms.EmailField(label = 'Enter your Email again!!')

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Emails are not matching!!")
