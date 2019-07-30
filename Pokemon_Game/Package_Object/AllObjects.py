from Object import *

#-------------------- Potion --------------------#
class Potion(Object):

	def __init__(self):
		self.small = False
		Object.__init__()

	def _remedy(self, creature):
		# TODO

#-------------------- Antidote --------------------#
class Antidote(Object):

	def __init__(self):
		Object.__init__()

	def _treat(self, creature):
		# TODO

#-------------------- Boost --------------------#
class Boost(Object):

	def __init__(self):
		Object.__init__()

	def _boost(self, creature):
		# TODO

#-------------------- CaptureKit --------------------#
class CaptureKit(Object):

	def __init__(self):
		Object.__init__()

	def _capture(self, creature):
		# TODO

#-------------------- Teleporter --------------------#
class Teleporter(Object):

	def __init__(self):
		Object.__init__()

	def _teleport(self, town):
		# TODO

#-------------------- RecipeObject --------------------#
class RecipeObject(Object):

	def __init__(self):
		Object.__init__()

#-------------------- Hormone --------------------#
class Hormone(Object):

	def __init__(self):
		Object.__init__()

	def _growUp(self, creature):
		# TODO

#-------------------- Residue --------------------#
class Residue(Object):

	def __init__(self):
		Object.__init__()

#-------------------- ReanimationKit --------------------#
class ReanimationKit(Object):

	def __init__(self):
		Object.__init__()

	def _revive(self, creature):
		# TODO

#-------------------- RecipeBook --------------------#
class RecipeBook(Object):

	def __init__(self):
		Object.__init__()

	def _book(self):
		# TODO

	def _readyToCook(self):
		# TODO

	def _cook(self, recipe):
		# TODO




