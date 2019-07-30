from abc, import ABC, abstractmethod

class Object(ABC):

	def __init__(self):
		self.name = ""
		self.price = 0
		super().__init__()
