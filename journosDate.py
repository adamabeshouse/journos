import datetime

def nextDate(date):
	d=datetime.date(int(date.split('/')[2]), int(date.split('/')[0]), int(date.split('/')[1]))
	n=d+datetime.timedelta(1)
	return datetimeToDate(n)

def prevDate(date):
	d=datetime.date(int(date.split('/')[2]), int(date.split('/')[0]), int(date.split('/')[1]))
	n=d+datetime.timedelta(-1)
	return datetimeToDate(n)


def today():
	return datetimeToDate(datetime.date.today())

def datetimeToDate(dt):
	ret = str(dt.month)+"/"+str(dt.day)+"/"+str(dt.year)
	return formatDate(ret)

def formatDate(s):
	try:
		y=datetime.date.today().year
		if len(s.split("/")) > 2:
			y=int(s.split("/")[2])
		m=int(s.split("/")[0])
		d=int(s.split("/")[1])
		ret=""
		if m<10:
			ret+="0"+str(m)
		else:
			ret+=str(m)
		ret+="/"

		if d<10:
			ret+="0"+str(d)
		else:
			ret+=str(d)
		ret+="/"

		if y<100:
			ret+="20"+str(y)
		else:
			ret+=str(y)
		return ret
	except:
		return -1

def min(_date1, _date2):
	date1=_date1.split("/")
	date2=_date2.split("/")
	if date1[2] < date2[2]:
		return _date1
	elif date1[2] > date2[2]:
		return _date2
	elif date1[0] < date2[0]:
		return _date1
	elif date1[0] > date2[0]:
		return _date2
	elif date1[1] < date2[1]:
		return _date1
	elif date1[1] > date2[1]:
		return _date2
	else:
		# arbitrary - they are equal
		return _date1
