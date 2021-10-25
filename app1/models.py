from django.db import models

# Create your models here.

class Employee(models.Model):
	name=models.CharField(max_length=30)
	date_of_birth=models.CharField(max_length=50)
	date_of_joining=models.CharField(max_length=50)
	
	gender=models.CharField(default=None,max_length=50)
	designation=models.CharField(max_length=50)
	reporting_manager=models.CharField(max_length=50)
	emp_image=models.ImageField(upload_to='static/app1/images',default='',blank=True)
	password=models.CharField(max_length=500)
	email=models.CharField(max_length=100,unique=True)