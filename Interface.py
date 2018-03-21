#-*-coding:utf-8-*-
"""Game Interface management"""
try:
	import sys,pygame

	from level         import *
	from gameThread    import *
	from pygame.locals import *
	from variables     import screen_size,case_scale
	from variables     import background_color as bg_clr
	from library       import draw_surface

except ImportError as err:
	print("Importation error occured at Interface.py :{}".format(err))
	sys(exit)

class Interface():
	"""class Interface for game interface managmement"""
	def __init__(self,level):
		pygame.init()
		self.screen_size = screen_size
		self.level = level
		self.level.class_elements()
		self.screen = pygame.display.set_mode(self.screen_size,RESIZABLE)
		self.background = draw_surface(self.screen.get_size(),bg_clr)
		self.game_over = False

	def handle_events(self):
		"""Handle player interaction with game"""
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_LEFT:
					pass
				elif event.key == K_RIGHT:
					pass
				elif event.key == K_DOWN:
					pass
				elif event.key == K_UP:
					pass

			if event.type == QUIT :
				self.game_over =  True

	def run_game(self):
		""" Running game main loop """
		# it'll be preferable to think about another system that a loop 
		# maybe i should use an asyncrhounous 
		pygame.key.set_repeat()
		while not self.game_over :
			self.handle_events()
			self.draw_level()
			pygame.display.update()

	def draw_level(self):
		"""drawing current level complete environment"""
		self.screen.blit(self.background,(0,0))
		self.level.draw(self.screen)
		return True

	def won(self):
		pass


	def apply_physics(self):
		"""This function will apply physical laws on game objects"""
		pass

	def scroll_screen(self):
		"""View scrolling management"""
		#use a thread for the scrolling task
		#use a game management task 