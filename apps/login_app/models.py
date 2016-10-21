from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
	def login(self, email, password):
		print ("login logic here")
		print("if successful login occurs pass back a tuple with (True,user)")
		print("if not successful return a tuple with (False, 'Login unsuccessful')")
		return ("I will be a future login method made by coding dojo students")

	def register(self, **kwargs):
		print ("register login here")
		print ("If successful login occurs pass back a tuple with (True, user)")
		pass


#create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	# confirm_password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	#this is new too!
	userManager = UserManager()

class Wish_list(models.Model):
	item = models.CharField(max_length=100)
	added_by = models.CharField(max_length=100)
	created_at= models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now = True)

	userManager = UserManager()
	objects = models.Manager()


#create models here