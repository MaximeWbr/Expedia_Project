from abc import abstractmethod

TypeEnum = ('Grass', 'Fire', 'Water', 'Darkness', 'Earth', 'Electric', 'Wind', 'Insect', 'Light')

#Class abstraite
class Type():

	def __init__(self,weakness, enumSize, nameType):
		self.weakness = weakness
		self.enumSize = enumSize
		self.dodge = 0	#Pourcentage de chance
		self.care = 0 #Pourcentage de l'attaque
		self.protection = 0 #Pourcentage de l'attaque
		self.poison = 0 #Pourcentage de l'attaque
		self.critic = 0 #Pourcentage de chance 
		self.nameType = nameType

	def _getEnumSize(self):
		return self.enumSize

	@abstractmethod
	def _powerEvolution(self, level):
		pass

	@abstractmethod
	def _healthEvolution(self, level):
		pass

	@abstractmethod
	def _isCaptured(self, health):
		pass

	@abstractmethod
	def _isEscaped(self, health):
		pass