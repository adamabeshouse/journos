import journosOut
import config
import datetime
import string

class Entry:
	general=""
	special={}
	date="01/01/2013"
	def getToday(self):
		journosOut.printBlue("What did you do today?")
		s=raw_input("... ").replace("|","/") # pipe is reserved for savefile delineation
		self.general=s
		conf=config.Config()
		conf.get()
		for q in conf.special_questions:
			journosOut.printBlue(q)
			s=raw_input("... ")
			self.special[q]=s
		d=datetime.date.today()
		self.date=str(d.month)+"/"+str(d.day)+"/"+str(d.year)
	
	def get(self,_date):
		journosOut.printPurple("You are about to complete an entry for "+_date)
		self.getToday()
		self.date=_date

	def to_s(self):
		ret=self.date+"|What did you do today?:"+self.general
		for q in self.special.keys():
			ret+="|"+q+":"+self.special[q]
		return ret
