'''
Created on 26 mai 2011

@author: guill
'''
from Gcode import *

# -*- coding: cp1252 -*-

prompt = "CNC >>"
gco = Gcode()

def HELP(self):
    print "ceci est l'aide"

def QUIT(self):
    print "bye"

def start():
    raw_comshell = ""
    while raw_comshell != "quit":
        
        raw_comshell = raw_input(prompt)
        comshell = raw_comshell.split(" ")
        command_parse(comshell)
        #imprimecrean(comshell)
        #execute la commande qui ce trouve dans comshell

def command_parse(raw):
    COMM.get(raw[0],HELP)(raw)

def imprimecrean(raw):
        n = ""
        for i in raw:
            n = n +" "+ i
        print n

COMM ={
       "help"   :HELP,
       "quit"   :QUIT,
        "G0"    :gco.G0com ,    # Interpolation lineaire en vitesse rapide
        "G1"    :gco.G1com ,    # Interpolation lineaire en vitesse programmee
#            "G2"    :"" ,            # Interpolation circulaire ("ou helicoidale") sens horaire
#            "G3"    :"" ,            # Interpolation circulaire ("ou helicoidale") sens antihoraire
#            "G7"    :"" ,            #
#            "G10"    :"" ,            #
#            "G17"    :"" ,            # Plan de travail XY
#            "G18"    :"" ,            # Plan de travail XZ
#            "G19"    :"" ,            # Plan de travail YZ
#            "G20"    :"" ,            #
        "G21"    :gco.G21com ,    #
#            "G30"    :"" ,            #
#            "G33"    :"" ,            # Filetage avec broche synchronisee
#            "G38"    :"" ,            #
        "G40"    :gco.G40com ,    # Annulation de la compensation de rayon d'outil
#            "G41"    :"" ,            # Compensation de rayon d'outil, a gauche profil
#            "G42"    :"" ,            # Compensation de rayon d'outil, a droite du profil
#            "G43"    :"" ,            #
        "G49"    :gco.G49com ,    #
#            "G53"    :"" ,            #
#            "G54"    :"" ,            #
#            "G59"    :"" ,            #
#            "G61"    :"" ,            # Mode trajectoire exacte
#            "G64"    :"" ,            # Mode trajectoire continue avec tolerance optionnelle
#            "G73"    :"" ,            #
#            "G76"    :"" ,            #
#            "G80"    :"" ,            # Revocation des codes modaux
#            "G81"    :"" ,            # Cycle de percage
#            "G82"    :"" ,            #
#            "G89"    :"" ,            #
       "G90"    :gco.G90com ,    # Deplacements en coordonnees absolues (par rapport a l'origine piece)
#            "G91"    :"" ,            # Deplacements en coordonnees relatives (incrementales)
#            "G92"    :"" ,            #
#            "G93"    :"" ,            # Vitesse inverse du temps (vitesse/distance)
#            "G94"    :"" ,            # Vitesse en unites par minute 
#            "G95"    :"" ,            # Vitesse en unites par tour
#            "G96"    :"" ,            #
#            "G97"    :"" ,            #
#            "G98"    :"" ,            # Retrait au point initial
#            "G99"    :"" ,            # Retrait sur R
}

if __name__ == '__main__':
    start()