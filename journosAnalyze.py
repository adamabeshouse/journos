import journosIn, journosOut
import datetime

class SubsetParams:
	def __init__(self):
		# entry parameters
		self.weekday=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
		self.timewindow=[datetime.date.today(), datetime.date.today()]
		# answer parameters
		self.startswith={} # answers to question Y that start with string X
		self.includes={} # answers to question Y that include string X
		

class StatisticParams:
	def __init__(self):
		self.window=1 # as in, the 'm' most used ... m is 'window'
		self.extreme=['least','most']


def analyzeMain():
	journosOut.printBlue("    __   ___   __ __ ____  __  __   ___    __ \n    ||  // \\\\  || || || \\\\ ||\\ ||  // \\\\  (( \\\n    || ((   )) || || ||_// ||\\\\|| ((   ))  \\\\ \n |__||  \\\\_//  \\\\_// || \\\\ || \||  \\\\_//  \\_))")
	journosOut.printPurple("Analysis console:")
	while True:
		inp = journosIn.getInput()
	
def subset(params):
	# in: parameters that define a subset
	# effect: create a file that contains exactly the entries specified by the parameters
	pass
