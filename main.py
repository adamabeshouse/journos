import sys
import os
import datetime
import backlog
import journosOut
import journosIn
import entry
import journosDate

# VALID COMMANDS:
#	journos
#	journos MM/DD/YYYY
#	journos read
#	journos read MM/DD/YYYY





# TODO: encryption
journosOut.printBlue("    __   ___   __ __ ____  __  __   ___    __ \n    ||  // \\\\  || || || \\\\ ||\\ ||  // \\\\  (( \\\n    || ((   )) || || ||_// ||\\\\|| ((   ))  \\\\ \n |__||  \\\\_//  \\\\_// || \\\\ || \||  \\\\_//  \\_))")

RUNTYPE="WRITE"
DATEFORMATERROR="Please input your date as MM/DD or MM/DD/YYYY"
d=datetime.date.today()
DATE=journosDate.today()

''' (I)  PARSE COMMAND ''' 
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
			journosOut.animPrintPurple("Would you like to fill out an entry for "+day+"? (Y/N)")
			if journosIn.isYes(journosIn.getInput()):
				ent=entry.Entry()
				ent.get(day)
				f=open("journal.journos","a")
				f.write(ent.to_s()+'\n')
				f.close()
			else: 
				ent=entry.Entry()
				ent.date=day
				f=open("journal.journos","a")
				f.write(ent.to_s()+'\n')
				f.close()
				journosOut.animPrintPurple("If you change your mind, type 'journos "+day+"'")
			journosOut.endSection()

	newEnt = entry.Entry()
	entSuccess = newEnt.readEntry(DATE)
	if entSuccess == 1:
		journosOut.animPrintBlue("Here's what you've written for "+("today" if DATE==journosDate.today() else DATE)+":")
		entry.printEntry(newEnt)

	_day="today" if DATE==journosDate.today() else DATE
	_create_type="fill out an" if entSuccess == 0 else "edit your"
	journosOut.animPrintPurple("Would you like to "+_create_type+" entry for "+_day+"? (Y/N)")

	if journosIn.isYes(journosIn.getInput()):
		if entSuccess == 0:
			newEnt.get(DATE)
			f=open("journal.journos","a")
			f.write(newEnt.to_s()+'\n')
			f.close()
		else:
			newEnt.edit(DATE)
			tmp=open("journal.journos.tmp","w")
			old=open("journal.journos","r")
			for line in old:
				if line.startswith(DATE):
					tmp.write(newEnt.to_s()+'\n')
				else:
					tmp.write(line)
			tmp.close()
			old.close()
			os.rename("journal.journos.tmp","journal.journos")

	else: 
		if entSuccess == 0:
			f=open("journal.journos","a")
			f.write(newEnt.to_s()+'\n')
			journosOut.animPrintPurple("If you change your mind, type 'journos "+journosDate.today()+"'")
		else:
			journosOut.animPrintPurple("If you change your mind, type 'journos "+journosDate.today()+"'")
	journosOut.endSection()
elif RUNTYPE=="READ":
	ent=entry.Entry()
	success = ent.readEntry(DATE)
	if success==1:
		entry.printEntry(ent)
	else:
		journosOut.printRed("No entry found on "+DATE)

