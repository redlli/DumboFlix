from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
	title=models.CharField(max_length=225)
	title_tag=models.CharField(max_length=225)
	ptype=models.CharField(max_length=225)
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	poster=models.TextField(max_length=225)
	
	def __str__(self):
		return self.title+ ' | ' +str(self.author)
	def  get_absolute_url(self):
		return reverse('post-details',args=(str(self.id)))
		#return reverse('home')
