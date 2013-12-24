import colorStack

def printBlue(s):
	colorStack.pushBlue()
	print(s)
	colorStack.popColor()

def printPurple(s):
	colorStack.pushPurple()
	print(s)
	colorStack.popColor()

def printGreen(s):
	colorStack.pushGreen()
	print(s)
	colorStack.popColor()

def printCyan(s):
	colorStack.pushCyan()
	print(s)
	colorStack.popColor()
