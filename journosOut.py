import colorStack
import os
import time
import sys

pauseLength=0.009

def out(s):
	sys.stdout.write(s)
	sys.stdout.flush()

def outBlue(s):
	colorStack.pushBlue()
	sys.stdout.write(s)
	sys.stdout.flush()
	colorStack.popColor()

def outPurple(s):
	colorStack.pushPurple()
	sys.stdout.write(s)
	sys.stdout.flush()
	colorStack.popColor()

def animPrint(s):
	for i in range(0,len(s)):
		sys.stdout.write(s[i])
		sys.stdout.flush()
		time.sleep(pauseLength)

def animPrintRed(s):
	colorStack.pushRed()
	animPrint("\n"+s+"\n")
	colorStack.popColor()

def animPrintBlue(s):
	colorStack.pushBlue()
	animPrint("\n"+s+"\n")
	colorStack.popColor()

def animPrintPurple(s):
	colorStack.pushPurple()
	animPrint("\n"+s+"\n")
	colorStack.popColor()

def animPrintGreen(s):
	colorStack.pushGreen()
	animPrint("\n"+s+"\n")
	colorStack.popColor()

def animPrintCyan(s):
	colorStack.pushCyan()
	animPrint("\n"+s+"\n")
	colorStack.popColor()

def printRed(s):
	colorStack.pushRed()
	print
	print(s)
	print
	colorStack.popColor()

def printBlue(s):
	colorStack.pushBlue()
	print
	print(s)
	print
	colorStack.popColor()

def printPurple(s):
	colorStack.pushPurple()
	print
	print(s)
	print
	colorStack.popColor()

def printGreen(s):
	colorStack.pushGreen()
	print
	print(s)
	print
	colorStack.popColor()

def printCyan(s):
	colorStack.pushCyan()
	print
	print(s)
	print
	colorStack.popColor()

def fullWidthBorder(border='~  o  '):
	rows,cols=os.popen('stty size','r').read().split()
	cols=int(cols)
	ret=""
	for i in range(0,cols): ret+=border[i%len(border)]
	return ret

def endSection():
	breakSize=3
	lineBr=""
	for i in range(0,breakSize): lineBr+='\n'
	lineBr+=fullWidthBorder()
	for i in range(0,breakSize): lineBr+='\n'
	animPrintRed(lineBr)
