import colorStack

def printBlue(s):
	colorStack.pushBlue()
	print(s)
	colorStack.popColor()

def printPurple(s):
	colorStack.pushPurple()
	print(s)
	colorStack.popColor()

def makeReadable(s):
	#line break every 80 characters, and add hyphen if you cut words in the middle
	moreReadable=''
	for i in range(len(s)):
		moreReadable += s[i]
		if i>0 and i%80==0:
			if s[i]!=' ' and i < len(s)-1:
				if s[i+1]!=' ':
					moreReadable += '-'
			moreReadable += '\n'
	return moreReadable
