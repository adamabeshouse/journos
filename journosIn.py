import datetime
import journosOut
from getpass import getpass

EOFERROR="Ctrl+C to quit"
def getPassword():
	try:
		return getpass()
	except EOFError:
		journosOut.printRed(EOFERROR)
		return getPassword()
			

def getInput():
	try:
		return raw_input("... ").replace("|","/") # pipe is reserved for savefile delineation
	except EOFError:
		journosOut.printRed(EOFERROR)
		return getInput()

def isYes(s):
	return s.lower().startswith("y")

