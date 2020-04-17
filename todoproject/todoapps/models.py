from django.db import models

# Create your models here.
DROPDOWN_CHOICES = [
	('Default','Default'),
	('Personal','Personal'),
	('Family','Family'),
	('Office','Office'),
]

class WorkList(models.Model):
	userwork = models.CharField(max_length=55,blank=False,null=False)
	textabtwork = models.TextField()
	listofwork = models.CharField(max_length=30,blank=False,null=False)
	dd_choice = models.CharField(max_length=32, choices=DROPDOWN_CHOICES)


	def __str__(self):
		return self.userwork






















