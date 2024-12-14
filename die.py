from random import randint

class Die():
	"""A class representing a single die"""
	def __init__(self,faces=6):
		"""Assume a 6 faced Die"""
		self.faces=faces
		
	def Roll(self):
		"""Return a random value between 1 and number of sides"""
		return randint(1,self.faces)
