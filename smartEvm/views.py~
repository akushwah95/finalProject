#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import time
from django.shortcuts import render
from django.template import RequestContext
from models import User, Vote
from forms import VoteForm

from pyfingerprint.pyfingerprint import PyFingerprint
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

def index(request):
	return render(request, 'home.html')

#about tab
def about(request):
	return render(request, 'about.html')

#contact tab	
def contact(request):
	return render(request, 'contact.html')

#authentication tab	
def authentication(request):
	return render(request, 'authentication.html')

#enrollment tab	
def enrollment(request):
	return render(request, 'enrollment.html')

#storing the vote
def vote(request):
	if request.method == "POST":
		form = VoteForm(request.POST)
		
		party_name = request.POST.get('party_name', '')
		hashes = request.POST.get('hashVal','')
			
		print "hash val : " + hashes
		print "party_id val : " + party_name
		
		vote_obj = Vote( party_name = party_name, hashes = hashes)
		vote_obj.save()
		
		return render(request, 'confirmation.html', { 'voted_now' : True, 'msg' : 'You have successfully voted.'})

#initiate sensor for authentication	
def auth(request):
	try:
		f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
		
		if ( f.verifyPassword() == False ):
			raise ValueError('The given fingerprint sensor password is wrong!')
			
	except Exception as e:
		return render(request, 'confirmation.html', { 'sensor_ni' : True, 'msg' : 'Fingerprint sensor could not be initialized.'})
		
	try:
		while ( f.readImage() == False ):
			pass
		
		f.convertImage(0x01)
		
		result = f.searchTemplate()
		
		positionNumber = result[0]
		accuracyScore = result[1]
		
		if ( positionNumber == -1 ):
			return render(request, 'confirmation.html', {'invalid_voter': True, 'msg': 'Voter data not present in the database'} )		
			
		f.loadTemplate(positionNumber, 0x01)
		
		characterics = str(f.downloadCharacteristics(0x01))
		
		hashVal = hashlib.sha256(characterics).hexdigest()
		
	except Exception as e:
		return render(request, 'confirmation.html', { 'sensor_ni' : True, 'msg': 'Unable to process your fingerprint. Please Try again.'} )
	
	print "hashVal :- " + hashVal
	all_obj = User.objects.all()
	
	print "all objects :- "
	for obj in all_obj:
		print obj.name 
		print obj.age 
		print obj.voter_id 
		print obj.hashes
		print type(obj.hashes)
	print type(hashVal)
	temp = unicode(hashVal)
	print temp
	print type(unicode(hashVal))
	
	try:
		obj = User.objects.get(hashes = temp)
		
	except ObjectDoesNotExist as invalid_user:
		return render(request, 'confirmation.html', {'invalid_voter': True, 'msg': 'Voter Data Not Present in the Database'} )
	
	try:
		vote_obj = Vote.objects.get(hashes = temp)
		
		if vote_obj :
			return render(request, 'confirmation.html', { 'has_voted': True, 'msg': 'Sorry %s , You have already voted to %s' % (obj.name, vote_obj.party_name)} )
	
	except ObjectDoesNotExist as valid_voter:
		print "Valid Voter"
		return render(request, 'vote.html', {'object': obj} )

#initiate sensor for enrollment
def pre_enroll(request):
	try:
		f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
		if ( f.verifyPassword() == False ):
			raise ValueError('The given fingerprint sensor password is wrong!')

	except Exception as e:
		return render(request, 'confirmation.html', { 'sensor_ni' : True, 'msg' : 'Fingerprint sensor could not be initialized.'})

	## Tries to enroll new finger
	try:
		print('Waiting for finger...')

		## Wait that finger is read
		while ( f.readImage() == False ):
			pass

		## Converts read image to characteristics and stores it in charbuffer 1
		f.convertImage(0x01)

		## Checks if finger is already enrolled
		result = f.searchTemplate()
		positionNumber = result[0]
		characterics = str(f.downloadCharacteristics(0x01))
		hashes = hashlib.sha256(characterics).hexdigest()
		
		if ( positionNumber >= 0 ):
			print('Template already exists at position #' + str(positionNumber))
			obj = User.objects.get(hashes = unicode(hashes))
			return render(request, 'confirmation.html', {'voter_present': True, 'msg': '%s Voter already enrolled in the database.' % obj.name} )
		
		print('Remove finger...')
		time.sleep(2)

		print('Waiting for same finger again...')

		while ( f.readImage() == False ):
			pass

		f.convertImage(0x02)

		if f.compareCharacteristics() != 0:
			f.createTemplate()
			characterics = str(f.downloadCharacteristics(0x01))
			hashes = hashlib.sha256(characterics).hexdigest()
			positionNumber = f.storeTemplate()
			print('New template position #' + str(positionNumber))
			return render(request, 'enroll.html', {'hashes': hashes} )
		else:
			return render(request, 'confirmation.html', {'finger_not_matched': True, 'msg': 'Fingerprint not matched. Please try again.'} )
	except Exception as e:
		return render(request, 'confirmation.html', {'enroll_failed': True, 'msg': 'Unable to enroll the voter. Please try again.'} )

#enroll the user
def enroll(request):
	if request.method == "POST":
		form = VoteForm(request.POST)	
	voter_id = request.POST.get('voter_id','')
	name = request.POST.get('name','')
	age = request.POST.get('age','')
	father_name = request.POST.get('father_name','')
	mother_name = request.POST.get('mother_name','')
	mobile_number = request.POST.get('mobile_number','')
	hashes = request.POST.get('hashes','')

	obj = User(voter_id=voter_id, name=name , age=age , father_name=father_name, mother_name=mother_name, mobile_number=mobile_number, 					hashes=hashes)
	obj.save()
	
	return render(request, 'confirmation.html', {'stored': True, 'msg': 'Voter Data Stored in the Database'} )	
