import colorStack
import os
import time
import sys

pauseLength=0.009

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

def endSection():
	breakSize=3
	border='~  o  '
	rows,cols=os.popen('stty size','r').read().split()
	cols=int(cols)
	lineBr=""
	for i in range(0,breakSize): lineBr+='\n'
	for i in range(0,cols): lineBr+=border[i%6]
	for i in range(0,breakSize): lineBr+='\n'
	animPrintRed(lineBr)
