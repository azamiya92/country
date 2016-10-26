from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Country(models.Model):
	name= models.CharField(max_length=255, unique=True)
	capital = models.CharField(max_length=255,null=True,blank=True)
	population = models.IntegerField(null=True,blank=True)
	flag = models.ImageField(null=True,blank=True,upload_to='flags')
	 
	def __unicode__(self):
		return self.name


class Review(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	country = models.ForeignKey(Country)
	user = models.ForeignKey(User)
	def __unicode__(self):
		return self.title