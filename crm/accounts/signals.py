from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Customer

def customer_profile(sender, instance, created, **kwargs):
	if created:
		#adding default group of 'customer' to all created user
		group = Group.objects.get(name='customer')
		instance.groups.add(group)

		#assigning a new user a Customer-Profile
		Customer.objects.create(
			user = instance,
			name = instance.username
		)
		print('Profile Created')

post_save.connect(customer_profile, sender=User)