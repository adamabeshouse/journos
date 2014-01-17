import sys
import os
import datetime
import backlog
import journosOut
import journosIn
import entry
import journosDate
import journosEncrypt
import journosSearch
import journosDir
from getpass import getpass
from Crypto.Cipher import DES
import signal
import editSpecialQ

# VALID COMMANDS:
#	journos
#	journos MM/DD/YYYY
#	journos read
#	journos read MM/DD/YYYY
#	journos changepw
#	journos dump


ENC_INIT_DONE=False
ENC_INIT_RUNNING=False
# Error Handling
def sigint_signal_handler(signal, frame):
	quit_gracefully()

def eof_handler():
	journosOut.printRed("Ctrl+C to quit")
	return

def quit_gracefully():
	if not enc.can_exit:
		journosOut.printRed("Cannot quit right now")
		return
	journosOut.printRed("Closing down...")
	if ENC_INIT_DONE:
		enc.exit()
	sys.exit(0)

signal.signal(signal.SIGINT, sigint_signal_handler)
# # # # # # # # #
def eatFlags():
	flags=[]
	newv=[]
	for i in range(0,len(sys.argv)):
		if sys.argv[i].startswith('-'):
			flags+=[sys.argv[i]]
		else:
			newv+=[sys.argv[i]]
	sys.argv=[newv[i] for i in range(0,len(newv))]
	return flags

journosOut.printBlue("    __   ___   __ __ ____  __  __   ___    __ \n    ||  // \\\\  || || || \\\\ ||\\ ||  // \\\\  (( \\\n    || ((   )) || || ||_// ||\\\\|| ((   ))  \\\\ \n |__||  \\\\_//  \\\\_// || \\\\ || \||  \\\\_//  \\_))")

# Get password, decrypt journal file
enc = journosEncrypt.JournosEncrypt()
ENC_INIT_RUNNING=True
enc.init()
ENC_INIT_RUNNING=False
ENC_INIT_DONE=True

RUNTYPE="WRITE"
DATEFORMATERROR="Please input your date as MM/DD or MM/DD/YYYY"
d=datetime.date.today()
DATE=journosDate.today()

''' (I)  PARSE COMMAND ''' 
if len(sys.argv) > 1 and sys.argv[1] == "changepw":
	enc.changePassword()
	quit_gracefully()

if len(sys.argv) > 1 and sys.argv[1] == "dump":
	enc.dump()
	quit_gracefully()

if len(sys.argv) > 1 and sys.argv[1].startswith("q"):
	editSpecialQ.editSpecialQ()
	quit_gracefully()

if len(sys.argv) > 1 and sys.argv[1].startswith("s"):
	flags=eatFlags()
	params=journosSearch.SearchParams()
	if len(sys.argv) > 2:
		if '-questions' in flags:
			params.questions=True
			params.answers=False
		elif '-answers' in flags:
			params.questions=False
			params.answers=True
		if '-case' in flags:
			params.case_sensitive=True

		journosSearch.search(sys.argv[2], params)
		quit_gracefully()
	else:
		journosOut.printRed("No search term specified")
		quit_gracefully()

if len(sys.argv) > 1:
	if sys.argv[1].lower().startswith("r"):
		RUNTYPE="READ"
	else:
		DATE=journosDate.formatDate(sys.argv[1])
		if DATE==-1: journosOut.printRed(DATEFORMATERROR)

if len(sys.argv) == 3:
	DATE=journosDate.formatDate(sys.argv[2])
	if DATE==-1: journosOut.printRed(DATEFORMATERROR)

''' (II)  EXECUTE COMMAND '''
if RUNTYPE=="WRITE":
	if DATE==journosDate.today():
		for day in backlog.daysMissing():
			journosOut.animPrintPurple("Would you like to fill out an entry for "+backlog.toString(day)+"? (Y/N)")
			if journosIn.isYes(journosIn.getInput()):
				ent=entry.Entry()
				ent.get(day)
				enc.can_exit=False
				f=open(journosDir.plainTextJourn(),"a")
				f.write(ent.to_s()+'\n')
				f.close()
				enc.can_exit=True
			else: 
				ent=entry.Entry()
				ent.date=day
				enc.can_exit=False
				f=open(journosDir.plainTextJourn(),"a")
				f.write(ent.to_s()+'\n')
				f.close()
				enc.can_exit=True
				journosOut.animPrintPurple("If you change your mind, type 'journos "+day+"'")
			journosOut.endSection()

	newEnt = entry.Entry()
	entSuccess = newEnt.readEntry(DATE)
	if entSuccess == 1:
		journosOut.animPrintBlue("Here's what you've written for "+("today" if DATE==journosDate.today() else DATE)+":")
		entry.printEntry(newEnt)

	_day="today, "+DATE if DATE==journosDate.today() else DATE
	_create_type="fill out an" if entSuccess == 0 else "edit your"
	journosOut.animPrintPurple("Would you like to "+_create_type+" entry for "+_day+"? (Y/N)")

	if journosIn.isYes(journosIn.getInput()):
		if entSuccess == 0:
			newEnt.get(DATE)
			enc.can_exit=False
			f=open(journosDir.plainTextJourn(),"a")
			f.write(newEnt.to_s()+'\n')
			f.close()
			enc.can_exit=True
		else:
			newEnt.edit(DATE)
			enc.can_exit=False
			tmp=open(journosDir.plainTextJournTmp(),"w")
			old=open(journosDir.plainTextJourn(),"r")
			for line in old:
				if line.startswith(DATE):
					tmp.write(newEnt.to_s()+'\n')
				else:
					tmp.write(line)
			tmp.close()
			old.close()
			os.rename(journosDir.plainTextJournTmp(),journosDir.plainTextJourn())
			enc.can_exit=True

	else: 
		if entSuccess == 0:
			enc.can_exit=False
			f=open(journosDir.plainTextJourn(),"a")
			f.write(newEnt.to_s()+'\n')
			f.close()
			enc.can_exit=True
			journosOut.animPrintPurple("If you change your mind, type 'journos "+journosDate.today()+"'")
		else:
			journosOut.animPrintPurple("If you change your mind, type 'journos "+journosDate.today()+"'")
	journosOut.endSection()
elif RUNTYPE=="READ":
	while True:
		ent=entry.Entry()
		success = ent.readEntry(DATE)
		if success==1:
			entry.printEntry(ent)
		else:
			journosOut.printRed("No entry found on "+DATE)
		journosOut.animPrintBlue("n -- Next      p -- Previous     e -- Edit")
		inp=journosIn.getInput().lower().strip()
		if inp=='n':
			DATE=journosDate.nextDate(DATE)
			continue
		elif inp=='p':
			DATE=journosDate.prevDate(DATE)
			continue
		elif inp=='e':
			newEnt = entry.Entry()
			if success==1:
				newEnt.edit(DATE)
				enc.can_exit=False
				tmp=open(journosDir.plainTextJournTmp(),"w")
				old=open(journosDir.plainTextJourn(),"r")
				for line in old:
					if line.startswith(DATE):
						tmp.write(newEnt.to_s()+'\n')
					else:
						tmp.write(line)
				tmp.close()
				old.close()
				os.rename(journosDir.plainTextJournTmp(),journosDir.plainTextJourn())
				enc.can_exit=True
			else:
				newEnt.get(DATE)
				enc.can_exit=False
				f=open(journosDir.plainTextJourn(),"a")
				f.write(newEnt.to_s()+'\n')
				f.close()
				enc.can_exit=True
			journosOut.endSection()
			continue
		else:
			break

# encrypt again
enc.exit()

