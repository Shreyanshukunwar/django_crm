from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User #default django User model

from .models import Order, Customer

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']
		widgets = {
			'name': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
			'phone': forms.TextInput(
				attrs={
					'class': 'form-control',
					'type': 'number'
					}
				),
			'email': forms.TextInput(
				attrs={
					'class': 'form-control',
					'type': 'email'
					}
				),
			}
		labels = {
			'name': 'Full name'
		}

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
