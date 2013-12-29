import sys
import tempfile
import journosOut
import journosDate
import config
import datetime
import string
import journosIn
import os
from subprocess import call

GENERAL="What did you do today?"
class Entry:
	section={}
	date="01/01/2013"
	
	def __init__(self):
		conf=config.Config()
		conf.get()
		self.section[GENERAL]=""
		for q in conf.special_questions:
			self.section[q]=""

	def getToday(self):
		journosOut.animPrintBlue(GENERAL)
		self.section[GENERAL]=journosIn.getInput()
		for q in self.section.keys():
			if q!=GENERAL:
				journosOut.animPrintBlue(q)
				self.section[q]=journosIn.getInput()
		d=datetime.date.today()
		self.date=str(d.month)+"/"+str(d.day)+"/"+str(d.year)
	
	def get(self,_date):
		if _date!=journosDate.today():
			journosOut.printPurple("You are about to complete an entry for "+_date)
		self.getToday()
		self.date=_date

	def edit(self,_date):
		ent=Entry()
		ent.readEntry(_date)
		initial_msg=ent.to_editable()
		EDITOR = os.environ.get('EDITOR','vim')
		with tempfile.NamedTemporaryFile(suffix=".tmp") as tmpfile:
			tmpfile.write(initial_msg)
			tmpfile.flush()
			call([EDITOR, tmpfile.name])
			tmpF=open(tmpfile.name,'r')
			text=tmpF.read()
			self.from_editable(text)

	def to_editable(self):
		ret="DO NOT EDIT ANY LINES THAT BEGIN WITH 'x|'\nLINE BREAKS WILL NOT BE RESPECTED\n\n"
		ret+="d|"+self.date+'\n\n'
		ret+="q|"+GENERAL+'\n\n'+self.section[GENERAL]+'\n\n'
		for q in self.section.keys():
			if q != GENERAL:
				ret+="q|"+q+'\n\n'+self.section[q]+'\n\n'
		return ret

	def from_editable(self, text):
		in_question=False
		lines=text.split('\n')
		current_question=""
		current_answer=""
		for line in lines:
			if line.startswith("d|"):
				self.date=line.split("d|")[1].strip()
			elif line.startswith("q|"):
				if current_question!="":
					self.section[current_question]=current_answer
				current_question=line.split("q|")[1].strip()
				current_answer=""
			else:
				current_answer+=line
		self.section[current_question]=current_answer
					
	def to_s(self):
		conf=config.Config()
		conf.get()
		ret=self.date+"|"+GENERAL+"|"+self.section[GENERAL]
		for q in conf.special_questions:
			ret+="|"+q+"|"+self.section[q]
		return ret

	def from_s(self, s):
		s=s.strip().split("|")
		self.date=s[0]
		i=1
		while i < len(s):
			self.section[s[i]]=s[i+1]
			i=i+2

	def readEntry(self, date):
		f=open("journal.journos","r")
		l=""
		success = 0
		for line in f:
			if line.startswith(date):
				l=line
				success = 1
				break
		if success == 0:
			return 0
		self.from_s(l)
		return 1

def printEntry(ent):
	rows,cols=os.popen('stty size','r').read().split()
	cols=int(cols)

	dateLine="#######    "+ent.date+"    "
	aboveLine="#######"
	belowLine="#######"

	for i in range(0,cols-len(dateLine)):
		dateLine+='#'

	for i in range(0,8+len(ent.date)):
		aboveLine+='`'
		belowLine+='.'
	for i in range(0,cols-(7+8+len(ent.date))):
		aboveLine+='#'
		belowLine+='#'
	
	header=aboveLine+'\n'+dateLine+'\n'+belowLine
	footer='\n'+journosOut.fullWidthBorder('_')+'\n'+journosOut.fullWidthBorder('#')+'\n'
	journosOut.printPurple(header)

	journosOut.printBlue(GENERAL)
	print
	print ent.section[GENERAL]
	for q in ent.section.keys():
		if q != GENERAL:
			journosOut.printBlue(q)
			print ent.section[q]
			
	journosOut.printPurple(footer)
