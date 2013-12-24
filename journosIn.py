import datetime

def getInput():
	# TODO: handle keyboard exception and stuff like that
	return raw_input("... ").replace("|","/") # pipe is reserved for savefile delineation

def isYes(s):
	return s.lower().startswith("y")

def formatDate(s):
	y=datetime.date.today().year
	if len(s.split("/")) > 2:
		y=int(s.split("/")[2])
	m=int(s.split("/")[0])
	d=int(s.split("/")[1])
	ret=""
	if m<10:
		ret+="0"+str(m)
	else:
		ret+=str(m)
	ret+="/"

	if d<10:
		ret+="0"+str(d)
	else:
		ret+=str(d)
	ret+="/"

	if y<100:
		ret+="20"+str(y)
	else:
		ret+=str(y)
	return ret

