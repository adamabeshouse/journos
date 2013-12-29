import datetime

def getInput():
	# TODO: handle keyboard exception and stuff like that
	return raw_input("... ").replace("|","/") # pipe is reserved for savefile delineation

def isYes(s):
	return s.lower().startswith("y")

