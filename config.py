import journosDir
import journosOut

class Config:
	special_questions=[]
	def get(self):
		f=open(journosDir.config(),"r")
		l=""
		for line in f:
			if line.startswith("special_questions"):
				l=line
				break
		self.special_questions=l.strip().split(":")[1].split("|")

	def set(self):
		f=open(journosDir.config(),"w")
		f.write("special_questions:")
		journosOut.printPurple("Your special questions are now the following:")
		for i in range(0,len(self.special_questions)):
			f.write(self.special_questions[i])
			journosOut.outBlue(self.special_questions[i]+'\n')
			if i < len(self.special_questions) -1:
				f.write("|")
		f.close()
