from appdirs import *
appname = "Journos"
appauthor = "Abesauce"
user_data_dir(appname, appauthor)
site_data_dir

def plainTextJourn():
	return user_data_dir(appname, appauthor)+'/plain.journos'

def plainTextJournTmp():
	return user_data_dir(appname, appauthor)+'/plain.journos.tmp'


def cipherTextJourn():
	return user_data_dir(appname, appauthor)+'/ciph.journos'
	
