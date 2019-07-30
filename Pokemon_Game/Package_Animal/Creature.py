import random
from Package_Animal.Type import TypeEnum
from Package_Animal.AllTypes import *

class Creature:

	def __init__(self, levelMax, valTypeEnum):
		self.experience = 0
		self.type = None
		

		typeEnum = TypeEnum[valTypeEnum]
		if typeEnum == 'Grass':
			self.type = Grass()
			self.name = GrassCreature[random.randrange(0, self.type._getEnumSize(), 1)]
		elif typeEnum == 'Fire':
			self.type = Fire()
			self.name = FireCreature[random.randrange(0, self.type._getEnumSize(), 1)]
		elif typeEnum == 'Water':
			self.type = Water()
			self.name = WaterCreature[random.randrange(0, self.type._getEnumSize(), 1)]
		elif typeEnum == 'Darkness':
			self.type = Darkness()
			self.name = DarknessCreature[random.randrange(0, self.type._getEnumSize(), 1)]
		elif typeEnum == 'Earth':
			self.type = Earth()
			self.name = EarthCreature[random.randrange(0, self.type._getEnumSize(), 1)]
		elif typeEnum == 'Electric':
			self.type = Electric()
			self.name = ElectricCreature[random.randrange(0, self.type._getEnumSize(), 1)]
		elif typeEnum == 'Wind':
			self.type = Wind()
			self.name = WindCreature[random.randrange(0, self.type._getEnumSize(), 1)]
		elif typeEnum == 'Insect':
			self.type = Insect()
			self.name = InsectCreature[random.randrange(0, self.type._getEnumSize(), 1)]
		elif typeEnum == 'Light':
			self.type = Light()
			self.name = LightCreature[random.randrange(0, self.type._getEnumSize(), 1)]

		self.level = random.randrange(1, levelMax, 1)
		self.health = self.type._healthEvolution(self.level)
		self.attack = self.type._powerEvolution(self.level)
		self.defense = self.type.defense
		self.name = ""


	def _print(self):
		print('type : '+str(type(self.type))+'\nname : '+self.name+'\nlevel : '+str(self.level))


	# Description: retourne False si en vie sinon True
	def _isDead(self):
		if self.health > 0:
			return False
		else:
			return True

	# Description: Determine si la creature est capturée a la fin du combat
	# Output: True: est capturée, False: c'est échapée
	def _getCapture(self):
		print("To do with the type")

	# Description: enfonction de l'expérience acquise, il determine si la creature passe un niveau
	def _levelEvolution(self):
		print("To do with the type of the creature")
		typeLimit = 10 	# Needs the type and the level to deteminate the limit
		if typeLimit <= self.experience:
			self.experience = 0
			self.level += 1 
	
	# Description: Add the experience earn and evaluate the level evolution
	# 				to update it, the evolution depend of the type
	def _addExperience(self, points):
		self.experience += points
		self._levelEvolution()
