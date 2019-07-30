from abc import ABC, abstractmethod

class Characters(ABC):

	def __init__(self):
		self.name = ""
		super().__init__()