
## yeh new file banaye
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxLengthValidator
from django.db.models.constraints import UniqueConstraint
from .models import User

class SignUpForm(forms.ModelForm):
    
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name=forms.CharField()
    aadhar_no=forms.CharField()
    mobile = forms.CharField()
    password = forms.CharField()
    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','aadhar_no','mobile', 'password']


class LoginForm(forms.Form):
    
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

    class Meta:
        fields = ['email', 'password']


