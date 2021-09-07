from django import forms 
from .models import Login, Register
class LoginForm(forms.ModelForm):

    class Meta:
        model  = Login
        fields = ['password', 'emailid']
    
class RegisterForm(forms.ModelForm):

    class Meta:
        model  = Register
        fields = ['password', 'username', 'name']