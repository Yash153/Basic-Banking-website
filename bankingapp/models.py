from django.db import models

class CustomerModel(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 90)
	email = models.EmailField(max_length = 100)
	balance = models.FloatField(max_length = 30)


	def __str__(self):
		return self.name

class TransferModel(models.Model):
	sender = models.CharField(max_length = 100)
	receiver = models.CharField(max_length = 100)
	amount = models.FloatField(max_length = 40)
	dt = models.CharField(max_length = 50)
	
	def __str__(self):
		return self.send + " to " + self.receive
