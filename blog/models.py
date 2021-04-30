from django.db import models
from userprofile.models import User_profileing
from django.contrib.auth.models import User

# Create your models here.
class publishedblog(models.Model):
	title =models.CharField(max_length= 500)
	content = models.CharField(max_length=3000)
	image= models.CharField(max_length=200)
	byuser= models.ForeignKey(User_profileing, on_delete=models.DO_NOTHING)
	date=models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title

class draftblog(models.Model):
	dtitle =models.CharField(max_length= 500)
	dcontent = models.CharField(max_length=3000)
	dimage= models.CharField(max_length=200)
	dbyuser= models.ForeignKey(User_profileing, on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.dtitle

class bookmarked(models.Model):
	bbyuser=models.ForeignKey(User,on_delete=models.DO_NOTHING)
	blog=models.ForeignKey(publishedblog,on_delete=models.DO_NOTHING)


