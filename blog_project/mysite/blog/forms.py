from django import forms
from .models import Post,Comment


class PostForm(form.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

        widgets = {
        'title':forms.TextInput(attrs={'class':'textinputclass'}) #class here is a css styling class..out class
        'text':forms.TextArea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        #editable-we edit it(comes from medium editor  library)
        # 2nd for styling
        # 3rd is our own class
        }

class CommentForm(form.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
        'author':forms.TextInput(attrs={'class':'textinputclass'}) #class here is a css styling class..out class
        'text':forms.TextArea(attrs={'class': 'editable medium-editor-textarea'})
