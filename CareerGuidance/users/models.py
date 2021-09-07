from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.

class Register(models.Model):

    id = models.IntegerField(max_length = 100,primary_key=True)
    username = models.CharField(max_length = 100,unique=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length = 100)

    def __init__(self,username,password,name):
        self.username = username
        self.password = password
        self.name = name
    @staticmethod
    def exists(username) ->bool:
            user = Users.get_user_by_username(username)
            return user!=None
    @staticmethod
    def get_user_by_username(username):
        return Users.query.filter_by(username = username).first()

    def save(self, *args, **kwargs):
        value = slugify(self.name)
        self.id = value
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "Users_register"
        

class Login(models.Model):

    password = models.CharField(max_length=50)
    emailid = models.EmailField(max_length = 100)

    def __init__(self,username,password,name):
        self.password = password
        self.emailid = emailid

    class Meta:
        db_table = "Users_login"
        
