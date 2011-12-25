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

def DEF(self):
    print ""

COMM ={
       "help"   :HELP,
       "quit"   :QUIT,
       ""       :DEF,
}


def start():
    raw_comshell = ""
    while raw_comshell != "quit":
        raw_comshell = raw_input(prompt)
        comshell = raw_comshell.split(" ")
        command_parse(comshell)

def command_parse(raw):
    return COMM.get(raw[0],HELP)(raw)


