from django.shortcuts import render
from . import models
from . import forms

# Create your views here.

def home(request):
	wl_form = forms.workForm()
	context = {
		'form' : wl_form
	}
	return render(request,'todoapps/home.html', context)


