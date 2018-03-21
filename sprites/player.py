from physics.vector import Vector
from variables import player_image,case_scale
class Player():
	def __init__(self,pos,level):
		self.size = Vector(0.8,1.2)
		self.pos = Vector(pos[0],pos[1])-(self.size-Vector(1,1))
		self.level = level
		self.hp = 100
		self.image = player_image
		self.velocity = Vector(0,0)
	def object_is_below(self):
		print ("this function wasn't developped yet")
	def collide_actor(self):
		print ("this function wasn't developped yet")
	def draw(self,screen):
		screen.blit(self.image,case_scale(self.pos.x,self.pos.y))
	def move(self):
		self.pos = self.pos + self.velocity
	def x_inside(self,x_point):
		return (x_point >= self.pos.x  and x_point<=self.pos.x+self.size.x)
	def y_inside(self,y_point):
		return (y_point >= self.pos.y  and y_point<=self.pos.y+self.size.y)
	def collide(self,tile):
		return (x_inside(tile.pos.x) or x_inside(tile.pos.x+tile.size.x)) and (y_inside(tile.pos.y) or y_inside(tile.pos.y+tile.size.x))
	def get_pos(self):
		return case_scale(self.pos.x,self.pos.y)