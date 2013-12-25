import datetime
import journosIn

def daysMissing():
	# give a list of days we need to collect an entry for
	cands=dayInterestWindow()
	f=open("journal.journos","r")
	for line in f:
		date=line.split("|")[0]
		if date in cands: cands.remove(date)
	return cands

def datetimeToDate(dt):
	ret = str(dt.month)+"/"+str(dt.day)+"/"+str(dt.year)
	return journosIn.formatDate(ret)

def dayInterestWindow():
	ret=[]
	for i in range(0,3):
		ret.append(datetimeToDate(datetime.date.today()-datetime.timedelta(days=i)))
	return ret
