import datetime
import journosIn
import journosDate

def daysMissing():
	# give a list of days we need to collect an entry for
	cands=dayInterestWindow()
	f=open("journal.journos","r")
	for line in f:
		date=line.split("|")[0]
		if date in cands: cands.remove(date)
	return cands


def dayInterestWindow():
	ret=[]
	for i in range(1,3):
		ret.append(journosDate.datetimeToDate(datetime.date.today()-datetime.timedelta(days=i)))
	return ret
