'''
Created on 1 juin 2011

@author: guill
'''
import sys
import shell
from Gcode import *
# -*- coding: cp1252 -*-
#verifie les arguments
#    -f fichier.nc    - charge une fichier Gcode
#    -c                 - mode commande manuel

def help(raw):
    print '"'+raw[1]+'"'+" n'est pas un argument valide, verifier vos parametres"
    print "\t-f fichier.nc\t- charge une fichier Gcode"
    print "\t-h\t\t- affiche l'aide"
    print "mode shell, sans argument(s) "

def loadfile(raw):
    monfichier = GParse(raw[2])
    monfichier.Parse()
    monfichier.affiche()

PARAM ={
    "-h":        help,
    "-f":        loadfile,
}


if __name__ == '__main__':
    #PARAM.get(len(sys.argv),SHELL)()
    raw = sys.argv
    if len(sys.argv) <= 1:
        shell.start()
    else:
        PARAM.get(raw[1], help)(raw)
    