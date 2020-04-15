from django.db import models

# Create your models here.


class WorkList(models.Model):
	userwork = models.CharField(max_length=55,blank=False,null=False)
	textabtwork = models.TextField()
	listofwork = models.CharField(max_length=30,blank=False,null=False)


	def __str__(self):
		return self.userwork






















