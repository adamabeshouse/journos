import colorStack
import os
import time

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
	colorStack.pushRed()
	rows,cols=os.popen('stty size','r').read().split()
	border=""
	rows=int(rows)
	cols=int(cols)
#	for i in range(0,cols):
		#if i%6==0:
		#	border+="~"
		#elif i%6==3:
		#	border+="o"
		#else:
		#	border+=" "
	#print
	#print(border)
	#print
	time.sleep(1)
	for i in range(0,rows):
		transitionTime=1.5 # in seconds
		time.sleep(transitionTime/rows)
		print
	colorStack.popColor()
