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
#journosOut.printBlue("  888888  .d88888b.  888     888 8888888b.  888b    888  .d88888b.   .d8888b.  \n    \"88b d88P\" \"Y88b 888     888 888   Y88b 8888b   888 d88P\" \"Y88b d88P  Y88b\n     888 888     888 888     888 888    888 88888b  888 888     888 Y88b.      \n     888 888     888 888     888 888   d88P 888Y88b 888 888     888  \"Y888b.   \n     888 888     888 888     888 8888888P\"  888 Y88b888 888     888     \"Y88b. \n     888 888     888 888     888 888 T88b   888  Y88888 888     888      \"888 \n     88P Y88b. .d88P Y88b. .d88P 888  T88b  888   Y8888 Y88b. .d88P Y88b  d88P \n     888  \"Y88888P\"   \"Y88888P\"  888   T88b 888    Y888  \"Y88888P\"   \"Y8888P\"  \n   .d88P                                                                       \n .d88P\"                                                                        \n888P\"                                                                          ")

RUNTYPE="WRITE"
d=datetime.date.today()
DATE=journosDate.today()

''' (I)  PARSE COMMAND ''' 
if len(sys.argv) > 1:
	if sys.argv[1].lower().startswith("r"):
		RUNTYPE="READ"
	else:
		# TODO: input error catching/safeguarding
		DATE=journosDate.formatDate(sys.argv[1])

if len(sys.argv) == 3:
	# TODO: input error catching/safeguarding
	DATE=journosDate.formatDate(sys.argv[2])


''' (II)  EXECUTE COMMAND '''
if RUNTYPE=="WRITE":
	if DATE=="today":
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
			f.write(todayEnt.to_s()+'\n')
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
			f.write(todayEnt.to_s()+'\n')
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

