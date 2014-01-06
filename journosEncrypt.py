from getpass import getpass
from Crypto.Cipher import DES
import journosOut,journosIn
import os
import string
import entry
import datetime
import journosDate
import journosDir

DECRYPTION_CONF="DO NOT DELETE THIS LINE"

class JournosEncrypt:
	def dump(self):
		date=journosDate.today().replace('/','_')
		dumpfile=open("journos_dump_"+date+".txt","w")
		ent=entry.latest()
		dumpfile.write(ent.toDump()+'\n')
		while ent.hasPrevious():
			ent.getPrevious()
			dumpfile.write(ent.toDump()+'\n')
		dumpfile.close()

	def createPassword(self):
		journosOut.animPrintPurple("Please enter a password")
		password = journosIn.getPassword()
		for i in range(0,max(0,8-len(password))):
			password+='X'
		confirmation = None
		while confirmation != password:
			journosOut.animPrintPurple("Please re-enter your password to confirm")
			confirmation = journosIn.getPassword()
			for i in range(0,max(0,8-len(confirmation))):
				confirmation+='X'
			if confirmation != password:
				journosOut.printRed("The passwords do not match. Please try again or keyboard interrupt to close the program and start over.")
		self.password=password[:8]

	def requestPassword(self):
		journosOut.animPrintPurple("Please enter your password")
		password = journosIn.getPassword()
		for i in range(0,max(0,8-len(password))):
			password+='X'
		password=password[:8]
		return password
	
	def verifyPassword(self, password):
		# as side effect, when succeeds, dumps decrypted version into journosDir.plainTextJourn(), and saves correct password in member variable
		obj = DES.new(password, DES.MODE_ECB)
		plainjourn = open(journosDir.plainTextJourn(), 'w')
		ciphjourn = open(journosDir.cipherTextJourn(),'r')
		ciphertext = ciphjourn.read()
		if obj.decrypt(ciphertext).startswith(DECRYPTION_CONF):
			plainjourn.write(obj.decrypt(ciphertext))
			plainjourn.close()
			ciphjourn.close()
			self.password = password
			return True
		else:
			plainjourn.close()
			ciphjourn.close()
			os.remove(journosDir.plainTextJourn())
			journosOut.printRed("Incorrect password.")
			return False

	def changePassword(self):
		self.createPassword()	


	def init(self):
		self.password=""
		self.can_exit=True
		if not os.path.exists(journosDir.cipherTextJourn()):
			newpass = self.createPassword()
			self.can_exit=False
			newfile = open(journosDir.plainTextJourn(),"w")
			newfile.write(DECRYPTION_CONF+'\n')
			self.can_exit=True
			return
		else:
			while True:
				password=self.requestPassword()
				self.can_exit=False
				verified=self.verifyPassword(password)
				self.can_exit=True
				if verified:
					return

	def exit(self):
		self.can_exit=False
		obj = DES.new(self.password, DES.MODE_ECB)
		ciphjourn = open(journosDir.cipherTextJourn(),'w')
		plainjourn = open(journosDir.plainTextJourn(),'r')
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
		os.remove(journosDir.plainTextJourn())
		
		

