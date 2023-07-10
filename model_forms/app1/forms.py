from app1.models import *
from django import forms

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'

class AccessForm(forms.ModelForm):
    class Meta:
        model=Access
        fields='__all__'
        labels={'name':'', 'author':'', 'date':''}

class Form_1(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        # fields=['topic_name','name']
        # exclude=['name']
        widgets={'name':forms.PasswordInput}
        labels={'name':'EnterName'}
        # help_texts={'name':'only Alphabets'}