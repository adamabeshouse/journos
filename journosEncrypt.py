from getpass import getpass
from Crypto.Cipher import DES
import journosOut
import os
import string

DECRYPTION_CONF="DO NOT DELETE THIS LINE"

class JournosEncrypt:
	password=""
	def createPassword(self):
		journosOut.animPrintPurple("Please enter a password")
		password = getpass()
		for i in range(0,max(0,8-len(password))):
			password+='X'
		confirmation = None
		while confirmation != password:
			journosOut.animPrintPurple("Please re-enter your password to confirm")
			confirmation = getpass()
			for i in range(0,max(0,8-len(confirmation))):
				confirmation+='X'
			if confirmation != password:
				journosOut.printRed("The passwords do not match. Please try again or keyboard interrupt to close the program and start over.")
		self.password=password[:8]

	def init(self):
		if not os.path.exists("ciphjourn.journos"):
			newpass = self.createPassword()
			newfile = open("journal.journos","w")
			newfile.write(DECRYPTION_CONF+'\n')
			return
		else:
			while True:
				journosOut.animPrintPurple("Please enter your password")
				password = getpass()
				for i in range(0,max(0,8-len(password))):
					password+='X'
				password=password[:8]
				obj = DES.new(password, DES.MODE_ECB)
				plainjourn = open('journal.journos', 'w')
				ciphjourn = open('ciphjourn.journos','r')
				ciphertext = ciphjourn.read()
				if obj.decrypt(ciphertext).startswith(DECRYPTION_CONF):
					plainjourn.write(obj.decrypt(ciphertext))
					plainjourn.close()
					ciphjourn.close()
					self.password = password
					return
				else:
					plainjourn.close()
					ciphjourn.close()
					os.remove('journal.journos')
					journosOut.printRed("Incorrect password.")
					continue

	def exit(self):
		obj = DES.new(self.password, DES.MODE_ECB)
		ciphjourn = open('ciphjourn.journos','w')
		plainjourn = open('journal.journos','r')
		plaintext = plainjourn.readlines()
		plaintext[0]=DECRYPTION_CONF+'\n'
		totallength=0
		for line in plaintext: totallength += len(line)
		adj=""
		for i in range(0,8-(totallength%8)):
			adj += 'X'
		plaintext[0]=DECRYPTION_CONF+adj+'\n'
		plaintext = string.join(plaintext,"")
		ciphjourn.write(obj.encrypt(plaintext))
		ciphjourn.close()
		plainjourn.close()
		# DEBUG: comment out the following line to debug stuff
		os.remove('journal.journos')
		
		

