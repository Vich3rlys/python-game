from physics.vector import Vector
from variables import gold_image,case

class Gold(Tile):
	"""Wall object class declaration"""
	def __init__(self,pos):
		self.image = gold_image
		self.pos = Vector(pos[0],pos[1])
		self.size = Vector(0.5,0.5)

	def draw(self,screen):
		screen.blit((self.pos.x+0.25)*case,(self.pos.y+0.25)*case)