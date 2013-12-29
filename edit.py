import sys, tempfile, os
from subprocess import call
EDITOR = os.environ.get('EDITOR','vim')

initial_message="INSERT INITIAL MESSAGE HERE"
with tempfile.NamedTemporaryFile(suffix=".tmp") as tempfile:
	tempfile.write(initial_message)
	tempfile.flush()
	call([EDITOR, tempfile.name])
	print("WE NOW PRINT THE CONTENTS OF THE TEMPORARY FILE")
	f=open(tempfile.name,'r')
	for line in f:
		print line.strip()
