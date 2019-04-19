from django.db import models

# Create your models here.
class Employee(models.Model):
	empno=models.IntegerField()
	empname=models.CharField(max_length=60)
	empadd=models.CharField(max_length=60)
	empsal=models.FloatField()

	def __str__(self):
		"""string representation of model"""
		return self.empname

