from django.forms import ModelForm
from . import models

class workForm(ModelForm):
	class Meta:
		model = models.WorkList
		fields = ['userwork','textabtwork','listofwork','dd_choice']