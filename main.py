import sys
import datetime
import backlog
import journosOut
import journosIn
import entry

# VALID COMMANDS:
#	journos
#	journos MM/DD/YYYY
#	journos read
#	journos read MM/DD/YYYY

# TODO: encryption
journosOut.printBlue("JOURNOS\n=======") # TODO: ASCII art

RUNTYPE="WRITE"
d=datetime.date.today()
DATE="today"

# (I)  PARSE COMMAND
if len(sys.argv) > 1:
	if sys.argv[1].lower().startswith("r"):
		RUNTYPE="READ"
	else:
		# TODO: input error catching/safeguarding
		DATE=journosIn.formatDate(sys.argv[1])

if len(sys.argv) == 3:
	# TODO: input error catching/safeguarding
	DATE=journosIn.formatDate(sys.argv[2])


# (II)  EXECUTE COMMAND
if RUNTYPE=="WRITE":
	for day in backlog.daysMissing():
		journosOut.printPurple("Would you like to fill out an entry for "+day+"? (Y/N)")
		if journosIn.isYes(journosIn.getInput()):
			ent=entry.Entry()
			ent.get(day)
			#TODO: write
		else: 
			ent=entry.Entry()
			ent.date=day
			#TODO: write (blank entry for that date)
			journosOut.printPurple("If you change your mind, type 'journos "+day+"'")
		journosOut.endSection()
	if DATE=="today":
		# TODO: editing old entries, doing an entry for one you've already done
		journosOut.printPurple("Would you like to fill out an entry for today? (Y/N)")
		if journosIn.isYes(journosIn.getInput()):
			ent=entry.Entry()
			ent.getToday()
			#TODO: write
		else:
			today=journosIn.formatDate(datetime.date.today())
			journosOut.printPurple("If you change your mind, type 'journos "+today+"'")
			quit()
	else:
		journosOut.printPurple("Would you like to fill out an entry for "+DATE+"? (Y/N)")
		if journosIn.isYes(journosIn.getInput()):
			ent=entry.Entry()
			ent.get(DATE)
			#TODO: write
		else:
			journosOut.printPurple("If you change your mind, type 'journos "+DATE+"'")
			quit()
	journosOut.endSection()
elif RUNTYPE=="READ":
	print "TO BE IMPLEMENTED: READING"

