import entry

class SearchParams:
	def __init__(self, q=True, a=True, c=False):
	# i.e., search question text? search answer text?
		self.questions = q
		self.answers = a
		self.case_sensitive = c

def search(text, searchParam=None):
	if not searchParam: 
		searchParam=SearchParams()
	matches=[]
	ent = entry.latest()
	if ent.contains(text,searchParam):
		matches.append(ent.date)
	while ent.hasPrevious():
		ent.getPrevious()
		if ent.contains(text,searchParam):
			matches.append(ent.date)
	
	printMatches(matches, text, searchParam)

		
	
def printMatches(matches, text, searchParam):
	ent = entry.Entry()
	for d in matches:
		ent.readEntry(d)
		ent.printSearchMatches(text, searchParam)
	
def find_all_helper(a_str, sub):
	start = 0
	while True:
		start = a_str.find(sub, start)
		if start == -1: return
		yield start
		start += len(sub)

def find_all(a_str, sub):
	# returns list of indexes in a_str where sub occurs
	return list(find_all_helper(a_str, sub))
