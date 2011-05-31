import sys
import shell
from Gcode import *
# -*- coding: cp1252 -*-
#verifie les arguments
#	-f fichier.nc	- charge une fichier Gcode
#	-c 				- mode commande manuel

def SHELL():
	shell.start()

def help():
	print "verifier vos parametres"
	print "\tf fichier.nc\t- charge une fichier Gcode"
	print "\tc\t\t- mode commande manuel"

def COMMAND1():
	print "Good1" + str(sys.argv)
	if sys.argv[1][0] == "f":
		monfichier = GParse(sys.argv[1][2:])
		monfichier.Parse()
		monfichier.affiche()
	#monfichier = GcodeParser(sys.argv[1])
	#print monfichier.getLineN(2)

def COMMAND2():
	print "Good2" + str(sys.argv)
	if sys.argv[1] == "f":
		monfichier = GParse(sys.argv[2])
		monfichier.Parse()


PARAM ={
	2:		COMMAND1,
	3:		COMMAND2,
}


PARAM.get(len(sys.argv),SHELL)()
#monfichier = GcodeParser(sys.argv[1])
#print monfichier.getLineN(2)
