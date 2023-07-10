from django import forms
f=[('MALE','male'),['FEMALE','female']]
g=[('PYTHON','python'),['JAVA','java']]
class student(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    date=forms.DateField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput())
    adress=forms.CharField(max_length=100,widget=forms.Textarea(attrs={'cols':20,'rows':2}))
    course =forms.ChoiceField(choices=g)
    gender=forms.MultipleChoiceField(choices=f)
    genders=forms.ChoiceField(choices=f,widget=forms.RadioSelect())
    courses=forms.MultipleChoiceField(choices=g,widget=forms.CheckboxSelectMultiple())