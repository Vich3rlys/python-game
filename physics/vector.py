"""class 'physics.Vector' used to handle two-dimensional positions and vectors"""
class Vector ():
	def __init__(self,x,y):
		self.x,self.y = x,y
	def __add__(self,vector):
		return Vector(self.x+vector.x , self.y+vector.y)
	def __sub__(self,vector):
		return Vector(self.x-vector.x , self.y-vector.y)
	def __mul__(self,vector):
		return Vector(self.x*vector.x, self.y*vector.y)
	def __str__(self):
		return "("+str(self.x)+","+str(self.y)+")"