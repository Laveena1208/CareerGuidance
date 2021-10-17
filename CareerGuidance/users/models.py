from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser , BaseUserManager # change
from .manager import UserManager #chnage


#chnage user class pura
class  User(models.Model):
    username = None
    email = models.EmailField(unique = True, blank=True)
    first_name  = models.CharField(max_length=100)
    last_name   =  models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    aadhar_no = models.CharField(max_length=100)
    email_token = models.CharField(max_length=100, null = True, blank = True)
    forget_password = models.CharField(max_length=100, null = True, blank = True)
    last_login = models.CharField(max_length=100, null = True, blank = True)
    last_logout = models.CharField(max_length=100, null = True, blank = True)
    password = models.CharField(max_length=100, default = "")

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    

### ya tak

class After10(models.Model):
    question=models.CharField(max_length=150,unique=True)

class After12Arts(models.Model):
    question=models.CharField(max_length=150,unique=True)

class After12Commerce(models.Model):
    question=models.CharField(max_length=150,unique=True)

class After12Science(models.Model):
    question=models.CharField(max_length=150,unique=True)

class After10colleges(models.Model):
    college_id = models.AutoField
    college_name = models.CharField(max_length=1000 ,  default="")
    college_address = models.CharField(max_length=1000 ,  default="")
    phone_number = PhoneNumberField(default="")
    website = models.URLField(max_length = 500, default="")

class After12engcolleges(models.Model):
    college_id = models.AutoField
    college_name = models.CharField(max_length=1000,  default="")
    college_address = models.CharField(max_length=1000,  default="")
    phone_number = PhoneNumberField(default="")
    website = models.URLField(max_length = 500, default="")


class After12medicolleges(models.Model):
    college_id = models.AutoField
    college_name = models.CharField(max_length=1000,  default="")
    college_address = models.CharField(max_length=1000,  default="")
    phone_number = PhoneNumberField(default="")
    website = models.URLField(max_length = 500, default="")

class After12commcolleges(models.Model):
    college_id = models.AutoField
    college_name = models.CharField(max_length=1000,  default="")
    college_address = models.CharField(max_length=1000,  default="")
    phone_number = PhoneNumberField(default="")
    website = models.URLField(max_length = 500, default="")

class After12artscolleges(models.Model):
    college_id = models.AutoField
    college_name = models.CharField(max_length=1000,  default="")
    college_address = models.CharField(max_length=1000,  default="")
    phone_number = PhoneNumberField(default="")
    website = models.URLField(max_length = 500, default="")