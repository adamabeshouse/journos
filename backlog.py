import datetime
import journosIn
import journosDate
import journosDir

dayHash={}
def daysMissing():
	# give a list of days we need to collect an entry for
	cands=dayInterestWindow()
	f=open(journosDir.plainTextJourn(),"r")
	for line in f:
		date=line.split("|")[0]
		if date in cands: cands.remove(date)
	return cands


def dayInterestWindow():
	ret=[]
	for i in [1,2]:
		ret.append(journosDate.datetimeToDate(datetime.date.today()-datetime.timedelta(days=i)))
	dayHash[ret[0]]="yesterday, "+ret[0]
	dayHash[ret[1]]="two days ago, "+ret[1]
	dayHash[journosDate.today()]="today, "+journosDate.today()
	return ret

def toString(day):
	return dayHash[day]
