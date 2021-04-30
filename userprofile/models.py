from django.db import models

# Create your models here.

class User_profileing(models.Model):
	username =models.CharField(max_length= 50)
	email = models.CharField(max_length=30)
	password= models.CharField(max_length=30)
	c_password= models.CharField(max_length=30)
	image=models.TextField()

	def __str__(self):
		return self.username