from Characters import *

#-------------------- Player --------------------#
class Player(Characters):

	def __init__(self):
		self.creatureList = []
		self.companionList = []
		self.objectList = []
		self.quest = ""
		self.worldMap = -1 # A MODIFIER UNE FOIS LA CLASSE CREER
		Charcaters.__init__()

#-------------------- Enemy --------------------#
class Enemy(Characters):

	def __init__(self):
		self.companionList = []
		self.objectList = []
		Characters.__init__()

#-------------------- Trader --------------------#
class Trader(Characters):

	def __init__(self):
		self.objectList = []
		Characters.__init__()

#-------------------- Doctor --------------------#
class Doctor(Characters):

	def __init__(self):
		Characters.__init__()