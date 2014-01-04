import config
import string
import os
from subprocess import call
import tempfile

def editSpecialQ():
	c = config.Config()
	c.get()
	initial_msg = "SKIPPING THIS LINE, write your questions separated by line breaks below\n"+string.join(c.special_questions, '\n')
	EDITOR = os.environ.get('EDITOR', 'vim')
	with tempfile.NamedTemporaryFile(suffix=".tmp") as tmpfile:
		tmpfile.write(initial_msg)
		tmpfile.flush()
		call([EDITOR, tmpfile.name])
		tmpF=open(tmpfile.name,'r')
		tmpF.readline()
		c.special_questions=[line.strip() for line in tmpF.readlines()]
	c.set()
