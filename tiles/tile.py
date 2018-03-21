from physics.vector import Vector
from variables import case,case_scale

class Tile():
	def __init__(self,pos,image,size):
		self.pos = Vector(pos[0],pos[1])
		self.image = image
		self.size = size
		self.rect = self.image.get_rect()

	def draw(self,screen):
		return screen.blit(self.image,case_scale(self.pos.x,self.pos.y))

	def scroll_draw(self,screen,scroll_distance):
		pass

	def get_pos(self):
		return self.pos

	def get_screen_pos(self,scroll_dif):
		# return the tile's position on the game window
		pos = case_scale(self.pos.x,self.pos.y)
		return [pos[0]-scroll_dif[0],pos[1]-scroll_dif[1]]

	def set_pos(self,position):
		self.pos = position