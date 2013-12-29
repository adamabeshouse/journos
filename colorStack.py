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
	sys.stdout.flush()

def pushPurple():
	colorStack.append(PURPLE)
	sys.stdout.write(PURPLE)
	sys.stdout.flush()

def pushCyan():
	colorStack.append(CYAN)
	sys.stdout.write(CYAN)
	sys.stdout.flush()

def pushRed():
	colorStack.append(RED)
	sys.stdout.write(RED)
	sys.stdout.flush()

def pushGreen():
	colorStack.append(GREEN)
	sys.stdout.write(GREEN)
	sys.stdout.flush()

def popColor():
	if len(colorStack)==1:
		colorStack.pop();
		sys.stdout.write(NOCOLOR)
	elif len(colorStack)>1:
		colorStack.pop();
		sys.stdout.write(colorStack[len(colorStack)-1])
	sys.stdout.flush()
