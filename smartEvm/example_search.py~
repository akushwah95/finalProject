#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint

def search_process():
	ff=open("/home/lohit/log.txt",'w')
	try:
		f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
		ff.write("Hello")
	except Exception as e:
		print('The fingerprint sensor could not be initialized!')
		print('Exception message: ' + str(e))
		exit(1)
		
	try:
		while ( f.readImage() == False ):
			pass
		ff.write("here1")
		f.convertImage(0x01)
		ff.write("here2")
		result = f.searchTemplate()
		ff.write(result)
		position = result[0]
		if ( position == -1 ):
			ff.write('No match found!')
			exit(0)
		 
		f.loadTemplate(positionNumber, 0x01)
		ff.write("here3")
		characterics = str(f.downloadCharacteristics(0x01))
		
		hashes = hashlib.sha256(characterics).hexdigest()
		ff.write("here4")
		print hashes
		
	except Exception as e:
		print 'Exception occurred'
		exit(1)
