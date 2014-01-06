import journosDir
import os

def ensure_dir(f):
	d = os.path.dirname(f)
	if not os.path.exists(d):
		os.makedirs(d)


try:
	import Crypto.Cipher
except ImportError:
	print 'Error, Module Crypto is required - try running "sudo pip install pycrypto" from the command line'

try:
	from appdirs import *
except ImportError:
	print 'Error, Module AppDirs is required - try running "sudo pip install appdirs" from the command line'

ensure_dir(journosDir.config())
c=open(journosDir.config(), "w")
c.write("special_questions:What grade would you give today?|Anything else on your mind?")
c.close()

