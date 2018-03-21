from physics.vector import Vector
from tiles.tile import Tile
from variables import wall_image,case

class Wall(Tile):
	"""Wall object class declaration"""
	def __init__(self,pos):
		self.image = wall_image
		self.size = Vector(1,1)
		Tile.__init__(self,pos,self.image,self.size)