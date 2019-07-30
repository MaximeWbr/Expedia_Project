from Package_Animal.Type import Type

GrassCreature = ('Acteon','Japa', 'Lotus', 'Neferti', 'Putzi', 'Xilo', 'Yucca', 'Zeste')
FireCreature = ('Caliot', 'Dakari', 'Furio', 'Minka', 'Salman', 'Sandro', 'Tropik')
WaterCreature = ('Bilbo', 'Bomba', 'Filomene', 'Hippop', 'Liseron', 'Perle', 'Radji')
DarknessCreature = ('Doggy', 'Quiro', 'Roxy', 'Rubis', 'Spectrum', 'Tucks')
EarthCreature = ('Euphoria', 'Gloup', 'Kanguro', 'Keops', 'Stonraid', 'Twins', 'Volibear')
ElectricCreature = ('Cachou', 'Calinou', 'Eko', 'Magic', 'Oxy', 'Takara', 'Whisky')
WindCreature = ('Benfica', 'Drago', 'Fly', 'Hulule', 'Kickster', 'Style', 'Virtuose', 'Vocipar')
InsectCreature = ('Disposide', 'Inca', 'Kalista', 'Voili', 'Waffy', 'Xeres')
LightCreature = ('Suki', 'Togo', 'Volcano', 'Wilo', 'Wulong', 'Xylo')

#---------------- Grass ----------------#
class Grass(Type):
	
	def __init__(self):
		Type.__init__(self, ('Fire', 'Insect'), 8, "Herbe")
		self.startingHealt = 3
		self.startingAttack = 0.9
		self.defense = 0.1

#	def _whip(self):
		# TODO

#	def _germ(self):
		# TODO

#	def _cut(self):
		# TODO

	def _powerEvolution(self, level):
		if level <= 10:
			return self.startingAttack * ((20/9)*(level-1) +5)
		elif level <= 25:
			return self.startingAttack * ((25/15)*(level-10)+25)
		elif level <= 40:
			return self.startingAttack * ((25/15)*(level-25)+50)
		elif level <= 50:
			return self.startingAttack * ((25/10)*(level-40)+75)
		elif level >= 50:
			return self.startingAttack * ((25/10)*(50-40)+75)

	def _healthEvolution(self, level):
		if level <= 10:
			return self.startingHealt * ((20/9)*(level-1) +5)
		elif level <= 25:
			return self.startingHealt * ((25/15)*(level-10)+25)
		elif level <= 40:
			return self.startingHealt * ((25/15)*(level-25)+50)
		elif level <= 50:
			return self.startingHealt * ((25/10)*(level-40)+75)
		elif level >= 50:
			return self.startingHealt * ((25/10)*(50-40)+75)

#	def _isCaptured(sekf, health):
		# TODO

#	def _isEscaped(self, health):
		# TODO


#---------------- Fire ----------------#
class Fire(Type):

	def __init__(self):
		Type.__init__(self, ('Water','Wind'), 7, "Feu")
		self.startingHealt = 2.9
		self.startingAttack = 1.1
		self.defense = 0

#	def _smoke(self):
		# TODO

#	def _burn(self):
		# TODO

#	def _magma(self):
		# TODO

	def _powerEvolution(self, level):
		if level <= 10:
			return self.startingAttack * ((20/9)*(level-1) +5)
		elif level <= 25:
			return self.startingAttack * ((25/15)*(level-10)+25)
		elif level <= 40:
			return self.startingAttack * ((25/15)*(level-25)+50)
		elif level <= 50:
			return self.startingAttack * ((25/10)*(level-40)+75)
		elif level >= 50:
			return self.startingAttack * ((25/10)*(50-40)+75)

	def _healthEvolution(self, level):
		if level <= 10:
			return self.startingHealt * ((20/9)*(level-1) +5)
		elif level <= 25:
			return self.startingHealt * ((25/15)*(level-10)+25)
		elif level <= 40:
			return self.startingHealt * ((25/15)*(level-25)+50)
		elif level <= 50:
			return self.startingHealt * ((25/10)*(level-40)+75)
		elif level >= 50:
			return self.startingHealt * ((25/10)*(50-40)+75)

#	def _isCaptured(sekf, health):
		# TODO

#	def _isEscaped(self, health):
		# TODO

#---------------- Water ----------------#
class Water(Type):

	def __init__(self):
		Type.__init__(self, ('Grass','Electric'), 7, "Eau")
		self.startingHealt = 2.9
		self.startingAttack = 1
		self.defense = 0.1

#	def _bublle(self):
		# TODO 

#	def _waterGun(self):
		# TODO

#	def _lifeWater(self):

	def _powerEvolution(self, level):
		if level <= 10:
			return self.startingAttack * ((20/9)*(level-1) +5)
		elif level <= 25:
			return self.startingAttack * ((25/15)*(level-10)+25)
		elif level <= 40:
			return self.startingAttack * ((25/15)*(level-25)+50)
		elif level <= 50:
			return self.startingAttack * ((25/10)*(level-40)+75)
		elif level >= 50:
			return self.startingAttack * ((25/10)*(50-40)+75)

	def _healthEvolution(self, level):
		if level <= 10:
			return self.startingHealt * ((20/9)*(level-1) +5)
		elif level <= 25:
			return self.startingHealt * ((25/15)*(level-10)+25)
		elif level <= 40:
			return self.startingHealt * ((25/15)*(level-25)+50)
		elif level <= 50:
			return self.startingHealt * ((25/10)*(level-40)+75)
		elif level >= 50:
			return self.startingHealt * ((25/10)*(50-40)+75)

#	def _isCaptured(sekf, health):
		# TODO

#	def _isEscaped(self, health):
		# TODO

#---------------- Darkness ----------------#
class Darkness(Type):

	def __init__(self):
		Type.__init__(self, ('Light'), 6, "Obscure")
		self.startingHealt = 3
		self.startingAttack = 1
		self.defense = 0

#	def _shadow(self):
		# TODO

#	def _ hipnosis(self):
		# TODO

#	def _demonSlash(self):
		# TODO

	def _powerEvolution(self, level):
		if level <= 10:
			return self.startingAttack * ((35/9)*(level-1) +15)
		elif level <= 25:
			return self.startingAttack * ((25/15)*(level-10)+50)
		elif level <= 40:
			return self.startingAttack * ((25/15)*(level-25)+75)
		elif level <= 50:
			return self.startingAttack * ((20/10)*(level-40)+100)
		elif level >= 50:
			return self.startingAttack * ((20/10)*(50-40)+100)

	def _healthEvolution(self, level):
		if level <= 10:
			return self.startingHealt * ((40/9)*(level-1) +15)
		elif level <= 25:
			return self.startingHealt * ((25/15)*(level-10)+55)
		elif level <= 40:
			return self.startingHealt * ((25/15)*(level-25)+80)
		elif level <= 50:
			return self.startingHealt * ((25/10)*(level-40)+105)
		elif level >= 50:
			return self.startingHealt * ((25/10)*(50-40)+105)

#	def _isCaptured(sekf, health):
		# TODO

#	def _isEscaped(self, health):
		# TODO

#---------------- Earth ----------------#
class Earth(Type):

	def __init__(self):
		Type.__init__(self, ('Grass','Fire'), 7, "Terre")
		self.startingHealt = 3
		self.startingAttack = 1
		self.defense = 0.2

#	def _kick(self):
		# TODO

#	def _earthquake(self):
		# TODO

#	def _avalanche(self):
		# TODO

	def _powerEvolution(self, level):
		if level <= 10:
			return self.startingAttack * ((12/9)*(level-1) +3)
		elif level <= 25:
			return self.startingAttack * ((20/15)*(level-10)+15)
		elif level <= 40:
			return self.startingAttack * ((30/15)*(level-25)+35)
		elif level <= 50:
			return self.startingAttack * ((30/10)*(level-40)+65)
		elif level >= 50:
			return self.startingAttack * ((30/10)*(50-40)+65)

	def _healthEvolution(self, level):
		if level <= 10:
			return self.startingHealt * ((27/9)*(level-1) +7)
		elif level <= 25:
			return self.startingHealt * ((26/15)*(level-10)+34)
		elif level <= 40:
			return self.startingHealt * ((20/15)*(level-25)+60)
		elif level <= 50:
			return self.startingHealt * ((25/10)*(level-40)+80)
		elif level >= 50:
			return self.startingHealt * ((25/10)*(50-40)+80)

#	def _isCaptured(sekf, health):
		# TODO

#	def _isEscaped(self, health):
		# TODO

#---------------- Electric ----------------#
class Electric(Type):

	def __init__(self):
		Type.__init__(self, ('Earth'), 7, "Electrique")
		self.startingHealt = 3
		self.startingAttack = 1
		self.defense = 0.1

#	def _flash(self):
		# TODO

#	def _shock(self):
		# TODO

#	def _thunder(self):
		# TODO

	def _powerEvolution(self, level):
		if level <= 10:
			return self.startingAttack * ((30/9)*(level-1) +10)
		elif level <= 25:
			return self.startingAttack * ((25/15)*(level-10)+40)
		elif level <= 40:
			return self.startingAttack * ((25/15)*(level-25)+65)
		elif level <= 50:
			return self.startingAttack * ((25/10)*(level-40)+90)
		elif level >= 50:
			return self.startingAttack * ((25/10)*(50-40)+90)

	def _healthEvolution(self, level):
		if level <= 10:
			return self.startingHealt * ((30/9)*(level-1) +10)
		elif level <= 25:
			return self.startingHealt * ((25/15)*(level-10)+40)
		elif level <= 40:
			return self.startingHealt * ((25/15)*(level-25)+65)
		elif level <= 50:
			return self.startingHealt * ((25/10)*(level-40)+90)
		elif level >= 50:
			return self.startingHealt * ((25/10)*(50-40)+90)

#	def _isCaptured(sekf, health):
		# TODO

#	def _isEscaped(self, health):
		# TODO

#---------------- Wind ----------------#
class Wind(Type):

	def __init__(self):
		Type.__init__(self, ('Water','Earth'), 8, "Vent")
		self.startingHealt = 3
		self.startingAttack = 1
		self.defense = 0

#	def _airFlow(self):
		# TODO

#	def _scratch(self):
		# TODO

#	def _storm(self):
		# TODO

	def _powerEvolution(self, level):
		if level <= 10:
			return self.startingAttack * ((23/9)*(level-1) +7)
		elif level <= 25:
			return self.startingAttack * ((25/15)*(level-10)+30)
		elif level <= 40:
			return self.startingAttack * ((25/15)*(level-25)+55)
		elif level <= 50:
			return self.startingAttack * ((25/10)*(level-40)+80)
		elif level >= 50:
			return self.startingAttack * ((25/10)*(50-40)+80)

	def _healthEvolution(self, level):
		if level <= 10:
			return self.startingHealt * ((12/9)*(level-1) +3)
		elif level <= 25:
			return self.startingHealt * ((20/15)*(level-10)+15)
		elif level <= 40:
			return self.startingHealt * ((30/15)*(level-25)+35)
		elif level <= 50:
			return self.startingHealt * ((30/10)*(level-40)+65)
		elif level >= 50:
			return self.startingHealt * ((30/10)*(50-40)+65)

#	def _isCaptured(sekf, health):
		# TODO

#	def _isEscaped(self, health):
		# TODO

#---------------- Insect ----------------#
class Insect(Type):

	def __init__(self):
		Type.__init__(self, ('Wind','Electric'), 7, "Insecte")
		self.startingHealt = 3
		self.startingAttack = 1
		self.defense = 0

#	def _sting(self):
		# TODO

#	def _bite(self):
		# TODO

#	def _infection(self):
		# TODO

	def _powerEvolution(self, level):
		if level <= 10:
			return self.startingAttack * ((23/9)*(level-1) +7)
		elif level <= 25:
			return self.startingAttack * ((25/15)*(level-10)+30)
		elif level <= 40:
			return self.startingAttack * ((25/15)*(level-25)+55)
		elif level <= 50:
			return self.startingAttack * ((25/10)*(level-40)+80)
		elif level >= 50:
			return self.startingAttack * ((25/10)*(50-40)+80)

	def _healthEvolution(self, level):
		if level <= 10:
			return self.startingHealt * ((12/9)*(level-1) +3)
		elif level <= 25:
			return self.startingHealt * ((20/15)*(level-10)+15)
		elif level <= 40:
			return self.startingHealt * ((30/15)*(level-25)+35)
		elif level <= 50:
			return self.startingHealt * ((30/10)*(level-40)+65)
		elif level >= 50:
			return self.startingHealt * ((30/10)*(50-40)+65)

#	def _isCaptured(sekf, health):
		# TODO

#	def _isEscaped(self, health):
		# TODO

#---------------- Light ----------------#
class Light(Type):

	def __init__(self):
		Type.__init__(self, ('Darkness'), 6, "Lumière")
		self.startingHealt = 3
		self.startingAttack = 1
		self.defense = 0

#	def _dazzel(self):
		# TODO

#	def _hipnosis(self):
		# TODO

#	def _godAttack(self):
		# TODO

	def _powerEvolution(self, level):
		if level <= 10:
			return self.startingAttack * ((35/9)*(level-1) +15)
		elif level <= 25:
			return self.startingAttack * ((25/15)*(level-10)+50)
		elif level <= 40:
			return self.startingAttack * ((25/15)*(level-25)+75)
		elif level <= 50:
			return self.startingAttack * ((20/10)*(level-40)+100)
		elif level >= 50:
			return self.startingAttack * ((20/10)*(50-40)+100)

	def _healthEvolution(self, level):
		if level <= 10:
			return self.startingHealt * ((40/9)*(level-1) +15)
		elif level <= 25:
			return self.startingHealt * ((25/15)*(level-10)+55)
		elif level <= 40:
			return self.startingHealt * ((25/15)*(level-25)+80)
		elif level <= 50:
			return self.startingHealt * ((25/10)*(level-40)+105)
		elif level >= 50:
			return self.startingHealt * ((25/10)*(50-40)+105)

#	def _isCaptured(sekf, health):
		# TODO

#	def _isEscaped(self, health):
		# TODO

