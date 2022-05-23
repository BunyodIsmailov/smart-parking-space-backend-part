from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    firstname 		= models.CharField(max_length=200)
    lastname 		= models.CharField(max_length=200)
    username 		= models.CharField(max_length=200,unique=True)
    password 		= models.CharField(max_length=200)
    createdat 		= models.DateTimeField(auto_now_add=True)
    updatedat 		= models.DateTimeField(auto_now=True)




class Client(models.Model):
    FirstName 		= models.CharField(max_length=200)
    LastName 		= models.CharField(max_length=200)
    CarModel 		= models.CharField(max_length=100)
    CarNumber 		= models.CharField(max_length=100)
    PhoneNumber 	= models.CharField(max_length=100)
    CreatedUserId   = models.ForeignKey(User,blank=False,null=True,on_delete=models.SET_NULL)
    CreatedAt 		= models.DateTimeField(auto_now_add=True)
    UpdatedAt 		= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.FirstName

class Server(models.Model):
    ServerIP 		= models.CharField(max_length=200)
    ServerPort 		= models.CharField(max_length=200)
    ServerLogin 	= models.CharField(max_length=200)
    ServerPassword  = models.CharField(max_length=200)
    CreatedUserld 	= models.ForeignKey(User,blank=False,null=True,on_delete=models.SET_NULL)

    def __str__(self):
      return self.ServerLogin

class Camera(models.Model):
    CamIP 			= models.CharField(max_length=200)
    CamPort 		= models.CharField(max_length=200)
    CamLogin 		= models.CharField(max_length=200)
    CamPassword 	= models.CharField(max_length=200)
    CreatedUserld 	= models.ForeignKey(User,blank=False,null=True,on_delete=models.SET_NULL)

    def __str__(self):
      return self.CamLogin


class Exiting(models.Model):
    ClientId 		= models.ForeignKey(Client,related_name='exiting',blank=False,null=True,on_delete=models.SET_NULL)
    ExitingTime 	= models.DateTimeField(auto_now_add=True)
    CreatedAt 		= models.DateTimeField(auto_now_add=True)
    UpdatedAt 		= models.DateTimeField(auto_now=True)

class Entering(models.Model):
    ClientId 		= models.ForeignKey(Client,related_name='enter',blank=False,null=True,on_delete=models.SET_NULL)
    EnteringTime 	= models.DateTimeField(auto_now_add=True)
    CreatedAt		= models.DateTimeField(auto_now_add=True)
    UpdatedAt 		= models.DateTimeField(auto_now=True)




