# run command

import subprocess

while True:
	print 
	cmd = raw_input("Shell=> ")

	c = subprocess.check_output(cmd , shell=True)

	print "\n",c

