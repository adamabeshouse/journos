import journosDir

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
