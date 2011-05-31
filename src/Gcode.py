# -*- coding: cp1252 -*-
class Gcode(object):
	"""docstring for Gcode"""
	def __init__(self):
		self.xyz = Coord()
		self.DICO_G_COM = {
			"G0"	:self.G0com ,	# Interpolation lineaire en vitesse rapide
			"G1"	:self.G1com ,	# Interpolation lineaire en vitesse programmee
#			"G2"	:"" ,			# Interpolation circulaire ("ou helicoidale") sens horaire
#			"G3"	:"" ,			# Interpolation circulaire ("ou helicoidale") sens antihoraire
#			"G7"	:"" ,			#
#			"G10"	:"" ,			#
#			"G17"	:"" ,			# Plan de travail XY
#			"G18"	:"" ,			# Plan de travail XZ
#			"G19"	:"" ,			# Plan de travail YZ
#			"G20"	:"" ,			#
			"G21"	:self.G21com ,	#
#			"G30"	:"" ,			#
#			"G33"	:"" ,			# Filetage avec broche synchronisee
#			"G38"	:"" ,			#
			"G40"	:self.G40com ,	# Annulation de la compensation de rayon d'outil
#			"G41"	:"" ,			# Compensation de rayon d'outil, a gauche profil
#			"G42"	:"" ,			# Compensation de rayon d'outil, a droite du profil
#			"G43"	:"" ,			#
			"G49"	:self.G49com ,	#
#			"G53"	:"" ,			#
#			"G54"	:"" ,			#
#			"G59"	:"" ,			#
#			"G61"	:"" ,			# Mode trajectoire exacte
#			"G64"	:"" ,			# Mode trajectoire continue avec tolerance optionnelle
#			"G73"	:"" ,			#
#			"G76"	:"" ,			#
#			"G80"	:"" ,			# Revocation des codes modaux
#			"G81"	:"" ,			# Cycle de percage
#			"G82"	:"" ,			#
#			"G89"	:"" ,			#
			"G90"	:self.G90com ,	# Deplacements en coordonnees absolues (par rapport a l'origine piece)
#			"G91"	:"" ,			# Deplacements en coordonnees relatives (incrementales)
#			"G92"	:"" ,			#
#			"G93"	:"" ,			# Vitesse inverse du temps (vitesse/distance)
#			"G94"	:"" ,			# Vitesse en unites par minute 
#			"G95"	:"" ,			# Vitesse en unites par tour
#			"G96"	:"" ,			#
#			"G97"	:"" ,			#
#			"G98"	:"" ,			# Retrait au point initial
#			"G99"	:"" ,			# Retrait sur R
		}
		self.DICO_M_COM = {
		}
		self.COM_LETTRE = {
			"G"		:self.GComm,
			"M"		:self.MComm,
			"F"		:self.FeedR,
			"("		:self.Comment,
			"T"		:self.ToolCom,
		}
	# TODO generer l'instruction G0 a envoyer a arduino
	def G0com(self, ligne):
		"""docstring for G0com"""
		return ligne
	
	# TODO generer l'instruction G1 a envoyer a arduino
	def G1com(self, ligne):
		"""docstring for G1com"""
		return ligne
	
	# TODO generer l'instruction G21 a envoyer a arduino
	def G21com(self, ligne):
		"""docstring for G21"""
		return "G21 :::"+ str(ligne)
	
	# TODO generer l'instruction G40 a envoyer a arduino
	def G40com(self, ligne):
		"""docstring for G40com"""
		return "G40 :::"+ str(ligne)
	
	# TODO generer l'instruction G49 a envoyer a arduino
	def G49com(self, ligne):
		"""docstring for G49"""
		return "G49 :::"+ str(ligne)
	
	# TODO generer l'instruction G90 a envoyer a arduino
	def G90com(self, ligne):
		"""docstring for G90com"""
		return "G90 :::"+ str(ligne)
	
	def GComm(self, lignefile):
		"""docstring for GComm"""
		#self.xyz.listtodic(lignefile)
		return self.DICO_G_COM.get(lignefile[0], self.Gnullcom)(self.xyz.listtodic(lignefile))
	
	def MComm(self, lignefile):
		"""docstring for MComm"""
		return self.DICO_M_COM.get(lignefile[0], self.Gnullcom)(lignefile[0])
	
	def FeedR(self, lignefile):
		"""docstring for FeedR"""
		return 	"feedR"
	
	def Comment(self, lignefile):
		"""docstring for Comment"""
		return 	lignefile
	
	def ToolCom(self, lignefile):
		"""docstring for toolCom"""
		return "toolcom"
	
	def Gnullcom(self, ligne):
		tmp = "la commande " + str(ligne)+ " nest pas encore implemente"
		return tmp

# TODO test
class Coord(object):
	"""docstring for Coord"""
	def __init__(self, x = 0, y = 0, z = 0):
		self.carte = {
			'x'		: x,
			'y'		: y,
			'z'		: z,
		}
	def listtodic(self, liste):
		"""docstring for listtodic"""
		self.carte.clear()
		for i in liste:
			if i[0] == "X": self.carte["x"] = i[1:]
			if i[0] == "Y": self.carte["y"] = i[1:]
			if i[0] == "Z": self.carte["z"] = i[1:]
		return self.carte
	
	def get_x(self):
		"""docstring pour get_y"""
		return self.carte['X']
	
	def get_y(self):
		"""docstring for get_y"""
		return self.carte['y']
	
	def get_z(self):
		"""docstring for get_z"""
		return self.carte['Z']
	
	def set_x(self):
		"""docstring for fname"""
		return self.carte['x']
	
	def set_y(self):
		"""docstring for fname"""
		return self.carte['y']
	
	def set_z(self):
		"""docstring for fname"""
		return self.carte['z']

class GParse():
	"""parse le fichier gcode"""
	def __init__(self, file):
		self.file = file
		self.Gc = Gcode()
		self.xyz = Coord()
		self.listeCode = []
	
	def Parse(self):
		"""Lecture et traitement du fichier gcode"""
		fileopen = open(self.file, 'r')
		contfile = fileopen.readlines()
		for l in contfile:
			self.listeCode.append(self.Gc.COM_LETTRE.get(l[0],self.Gc.Comment)(l.split(' ')))
		fileopen.close()
	
	def affiche(self):
		"""docstring for affiche"""
		for i in self.listeCode:
			print i
	

