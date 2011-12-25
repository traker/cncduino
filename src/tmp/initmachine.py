from comm import *
# -*- coding: cp1252 -*-
"""
initialise la machine
	- verifie que arduino est connecte
	- cherche l'origne machine a l'aide des fin de course 
"""
class InitMachine(object):
	"""docstring for InitMachine"""
	def __init__(self):
		#self.SOCKET = port_serie
		self.CONNECT = ComSocket()
		self.CONNECT.connect()
