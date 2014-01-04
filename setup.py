import journosDir
import os

def ensure_dir(f):
	d = os.path.dirname(f)
	if not os.path.exists(d):
		os.makedirs(d)

ensure_dir(journosDir.config())
c=open(journosDir.config(), "w")
c.write("special_questions:What grade would you give today?|Anything else on your mind?")
c.close()

