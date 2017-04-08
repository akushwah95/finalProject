from django import forms

class VoteForm(forms.Form):
	hashes = forms.CharField(max_length = 64)
	party_id = forms.IntegerField()
	
	def __str__(self):
		return self.hashes
		
class EnrollForm(forms.Form):
	voter_id = forms.IntegerField()
	name = forms.CharField(max_length = 40)
	age = forms.IntegerField()
	hashes = forms.CharField(max_length = 64)
	father_name = forms.CharField(max_length = 40)
	mother_name = forms.CharField(max_length = 40)
	mobile_number = forms.CharField(max_length = 10)
	
	def __str__(self):
		return self.hashes
