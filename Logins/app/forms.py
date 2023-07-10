from django import forms
from app.models import *
class LoginForm(forms.Form):
    Username=forms.CharField(max_length=100)
    Password=forms.CharField(max_length=15,widget=forms.PasswordInput)
    Re_EnterPassword=forms.CharField(max_length=15,widget=forms.PasswordInput)
      
    def clean(self):
        Pw=self.cleaned_data['Password']
        Rw=self.cleaned_data['Re_EnterPassword']
        if Pw!=Rw:
            raise forms.ValidationError("Password not Matched!!")

class RegisterForm(forms.Form):
    Username=forms.CharField(max_length=100)
    Password=forms.CharField(max_length=15,widget=forms.PasswordInput)
    def clean(self):
        A=self.cleaned_data['Username']
        B=LoginForm.self.cleaned_data['Username']
        Pw=self.cleaned_data['Password']
        Rw=LoginForm.self.cleaned_data['Password']
        if Pw!=Rw and A!=B:
            raise forms.ValidationError("Password not Matched!!")

class StudentForm(forms.Form):
    Sid=forms.IntegerField()
    Sname=forms.CharField(max_length=20)
    Sage=forms.IntegerField()
    Semail=forms.EmailField()
    JDate=forms.DateField()
    
