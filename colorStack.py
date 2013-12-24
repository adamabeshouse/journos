colorStack=[]
BLUE='\033[94m'
PURPLE='\033[35m'
NOCOLOR='\033[0m'
RED='\033[93m'
GREEN='\033[92m'
CYAN='\033[36m'

def pushBlue():
	colorStack.append(BLUE)
	print BLUE

def pushPurple():
	colorStack.append(PURPLE)
	print PURPLE

def pushCyan():
	colorStack.append(CYAN)
	print CYAN

def pushRed():
	colorStack.append(RED)
	print RED

def pushGreen():
	colorStack.append(GREEN)
	print GREEN

def popColor():
	if len(colorStack)==1:
		colorStack.pop();
		print NOCOLOR
	elif len(colorStack)>1:
		colorStack.pop();
		print colorStack[len(colorStack)-1]