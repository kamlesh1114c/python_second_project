from django.db import models

# Create your models here.

class Contact(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	subject=models.CharField(max_length=100)
	message=models.TextField()

	def __str__(self):
		return self.name

class User(models.Model):
	username=models.CharField(max_length=50)
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	mobile=models.IntegerField(default="")
	profile_pic=models.ImageField(upload_to="profile_pic/",default="")

	def __str__(self):
		return self.username   

class Hotel_Ditaile(models.Model):
	destination=models.CharField(max_length=50)
	room=models.IntegerField()
	adult=models.IntegerField()
	children=models.IntegerField()
	check_in=models.DateField(default="")
	check_out=models.DateField(default="")

	def __str__(self):
		return self.destination		
	