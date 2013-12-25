import sys

colorStack=[]
BLUE='\033[94m'
PURPLE='\033[35m'
NOCOLOR='\033[0m'
RED='\033[91m'
GREEN='\033[92m'
CYAN='\033[36m'

def pushBlue():
	colorStack.append(BLUE)
	sys.stdout.write(BLUE)

def pushPurple():
	colorStack.append(PURPLE)
	sys.stdout.write(PURPLE)

def pushCyan():
	colorStack.append(CYAN)
	sys.stdout.write(CYAN)

def pushRed():
	colorStack.append(RED)
	sys.stdout.write(RED)

def pushGreen():
	colorStack.append(GREEN)
	sys.stdout.write(GREEN)

def popColor():
	if len(colorStack)==1:
		colorStack.pop();
		sys.stdout.write(NOCOLOR)
	elif len(colorStack)>1:
		colorStack.pop();
		sys.stdout.write(colorStack[len(colorStack)-1])
