import journosOut
import config
import datetime
import string
import journosIn

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
		journosOut.printBlue(GENERAL)
		self.section[GENERAL]=journosIn.getInput()
		for q in self.section.keys():
			if q!=GENERAL:
				journosOut.printBlue(q)
				self.section[q]=journosIn.getInput()
		d=datetime.date.today()
		self.date=str(d.month)+"/"+str(d.day)+"/"+str(d.year)
	
	def get(self,_date):
		journosOut.printPurple("You are about to complete an entry for "+_date)
		self.getToday()
		self.date=_date

	def to_s(self):
		conf=config.Config()
		conf.get()
		ret=self.date+"|"+GENERAL+":"+self.section[GENERAL]
		for q in conf.special_questions:
			ret+="|"+q+":"+self.section[q]
		return ret

	def from_s(self, s):
		s=s.strip().split("|")
		self.date=s[0]
		for i in range(1,len(s)):
			QnA=s[i].split(":")
			self.section[QnA[0]] = QnA[1]

def readEntry(date):
	f=open("journal.journos","r")
	l=""
	for line in f:
		if line.startswith(date):
			l=line
			break
	ent=Entry()
	ent.from_s(l)
	return ent
