import datetime

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

