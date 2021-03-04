from django.db import models

# Create your models here.

class RegEmail(models.Model):
    Email_addr = models.EmailField(max_length=25,unique=True)

    def __str__(self):
        return self.Email_addr

class UserInfo(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    mail = models.ForeignKey(RegEmail, on_delete=models.CASCADE)

    def __str__(self):
        return self.First_name + " " + self.Last_name
