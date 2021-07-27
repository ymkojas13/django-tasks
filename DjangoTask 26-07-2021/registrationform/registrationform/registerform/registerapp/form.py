from django import forms
from .models import regmode
class rforms(forms.Form):
    fname=forms.CharField(max_length=50)
    lname=forms.CharField(max_length=50)
    email=forms.EmailField()
    contact=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput,max_length=50)
    confirmpassword=forms.CharField(widget=forms.PasswordInput,max_length=50)

class UserRegForm(forms.ModelForm):
    class Meta:
        model = regmode
        fields = ('fname', 'lname', 'email', 'contact','password','confirmpassword')

    field_order = ['fname', 'lname', 'email','contact' 'password','confirmpassword']