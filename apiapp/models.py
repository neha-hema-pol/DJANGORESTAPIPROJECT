from django.db import models

# Create your models here.

class Destination:
    email: str
    password: str
    name: str
    username: str

class User1(models.Model):
    
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    mobile = models.IntegerField(null=True)
    password = models.IntegerField(null=True)

    def __str__(self):
        return (name, email, mobile, password)


class Register(models.Model):
    
    Uname = models.CharField(max_length=70)
    Uemail = models.EmailField(max_length=70)
    Umobile = models.IntegerField(null=True)
    Upassword = models.IntegerField(null=True)

    def __str__(self):
        return (Uname, Uemail, Umobile, Upassword)


