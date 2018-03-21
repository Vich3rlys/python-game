from physics.vector import Vector
from tiles.tile import Tile
from variables import lava_image
class Lava(Tile):
	"""Wall object class declaration"""
	def __init__(self,pos,lava_type):
		self.type = lava_type
		self.image = lava_image
		self.velocity=Vector(None,None)
		self.size = Vector(1,1)
		Tile.__init__(self,pos,self.image,self.size)

	def move(self):
		pass