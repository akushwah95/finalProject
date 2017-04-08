from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	voter_id = models.IntegerField(unique = True)
	name = models.CharField(max_length = 40)
	age = models.IntegerField()
	hashes = models.CharField(max_length = 64, unique = True)
	father_name = models.CharField(max_length = 40)
	mother_name = models.CharField(max_length = 40)
	mobile_number = models.CharField(max_length = 10)
	
	def __str__(self):
		return self.hashes
		
class Vote(models.Model):
	hashes = models.CharField(max_length = 64, unique = True)
	party_name = models.CharField(max_length = 30)
	
	def __str__(self):
		return self.hashes
		
class Party_name(models.Model):
	party_name = models.CharField(max_length = 30, unique = True)
	
	def __str__(self):
		return self.party_name
