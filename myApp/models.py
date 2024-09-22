from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER=[
        ('admin','Admin'),
        ('viewer','Viewer'),
    ]

    usertype=models.CharField(choices=USER,max_length=100,null=True)

    def __str__(self) -> str:
        return f"{self.username}-{self.first_name}-{self.last_name}"
    

class Resume_model(models.Model):
    GENDER=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]

    gender_type=models.CharField(max_length=100,null=True,choices=GENDER)
     

    user=models.OneToOneField(CustomUser,null=True,on_delete=models.CASCADE)


    contact=models.CharField(max_length=100, null=True)
    designation=models.CharField(max_length=100, null=True)
    email=models.CharField(max_length=100, null=True)
    age=models.CharField(max_length=100, null=True)
    img=models.ImageField(upload_to='Media/img',null=True)
    carrier_summery=models.CharField(max_length=100,null=True)

    def __str__(self) -> str:
        return f"{self.user}"
    


class Language_model(models.Model):
    PROPHECIENCY=[
        ('beginner','Beginner'),
        ('intermidiate','Intermidiate'),
        ('other','Expert'),
    ]

    propheciency_type=models.CharField(max_length=100,null=True,choices=PROPHECIENCY)
     

    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)


    language_name=models.CharField(max_length=100, null=True)


    def __str__(self) -> str:
        return f"{self.user}"
    

class SKILL_MODEL(models.Model):

          
    PROFHECEENCY=[
        ('high','HIGH'),
        ('low','LOW'),
        ('medium','MEDIUM'),
    ]
    PROFHECEENCY=models.CharField(max_length=100,null=True,choices=PROFHECEENCY)
    user=models.OneToOneField(CustomUser,null=True,on_delete=models.CASCADE)
    skill_name=models.CharField(max_length=100, null=True)


def __str__(self) -> str:
    return f"{self.user}"


class INTERMEDIATE_MODEL(models.Model):
    skill_name=models.CharField(max_length=100)


    
    def __str__(self) -> str:
        return f"{self.skill_name}"