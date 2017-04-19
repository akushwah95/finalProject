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
	hashes = forms.CharField(max_length = 2700)
	father_name = forms.CharField(max_length = 40)
	mother_name = forms.CharField(max_length = 40)
	mobile_number = forms.CharField(max_length = 10)
	
	def __str__(self):
		return self.hashes

class PartyNameForm(forms.Form):
	def __init__(self, party_names, *args, **kwargs):
		super(PartyNameForm, self).__init__(*args, **kwargs)
		# now we add each question individually
		for i, party_name in enumerate(party_names):
			self.fields['Party %d' % i] = forms.ChoiceField(label=party_name)
