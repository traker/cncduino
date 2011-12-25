import serial
import os

# -*- coding: cp1252 -*-
class ComSocket(object):
	"""ComSocket gere la connexion entre chumby et arduino"""
	def __init__(self):
		#self.portcom = portcom
		#self.se = serial.Serial(self.scan())
		self.CONNECTION = serial.Serial()


	def scan(self):
		"""
		scan for available ports. return a list of tuples (num, name)
		"""
		available = []
		for i in range(256):
			try:
				s = serial.Serial(i)
				available.append( (i, s.portstr))
				s.close()   # explicit close 'cause of delayed GC in java
			except serial.SerialException:
				pass
		return available
	
	def connect(self):
		"""selon l'os configure le port puis se connecte"""
		if	os.name != "nt":
			#if os.uname()[0] == "Linux":
			if os.name == "posix":
				self.CONNECTION.port = '/dev/ttyUSB0'
				self.CONNECTION.open()
		else:
			intscn = self.scan()
			if len(intscn) == 0:
				print 'aucune carte arduino est connecté'
			else:
				self.CONNECTION.port = self.scan()
				self.CONNECTION.open()
	
	def stopc(self):
		"""stop la connection entre chumby et arduino"""
		self.CONNECTION.close()
	
	def get_connect(self):
		"""renvoi l'instance de l'objet CONNECTION"""
		return self.CONNECTION

