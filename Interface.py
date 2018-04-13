#-*-coding:utf-8-*-
"""Game Interface management"""
try:
	import sys,pygame

	from level         import *
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
		self.game_step = 90 # 1000/ 90 seconds

	def is_game_over(self):
		return  (self.level.player.is_alive() == False ) or (self.won == True)

	def handle_events(self):
		"""Handle player interaction with game"""
		pressed = pygame.key.get_pressed()
		if self.level.player.object_below() == None:
			print(self.level.player.pos.x)

		if pressed[K_LEFT]:
			if self.level.player.left() > 0 :
				self.level.player.add_action("left")

		if pressed[K_RIGHT]:
			if self.level.player.right() < len(self.level.map[0]):
				self.level.player.add_action("right")

		if pressed[K_DOWN]:
			self.level.player.add_action("crouch")

		if pressed[K_UP] or pressed[K_SPACE]:
			self.level.player.add_action("jump")

		for e in pygame.event.get():
			if e.type == QUIT :
				self.game_over =  True

	def display_hud(self):
		print ("this method wasn't developped yet ")

	def animate(self):
		""" """
		self.level.animate_sprites()

	def run_game(self):
		""" Running game main loop """
		clock  = pygame.time.Clock()
		pygame.key.set_repeat()
		while not self.game_over :
			self.handle_events()
			self.animate()
			# check if game is over 

			#update screen 
			self.draw_level()

			pygame.display.update()
			clock.tick(self.game_step) #wait 1000/90 seconds


	def draw_level(self):
		"""drawing current level complete environment"""
		self.screen.blit(self.background,(0,0))
		#print (self.scroll_screen())
		#sys.exit(0)
		self.level.draw(self.screen, self.scroll_screen())
		return True

	def won(self):
		pass

	def apply_physics(self, step ):
		"""This function will apply physical laws on game objects"""
		pass

	def scroll_screen(self):
		"""View scrolling management"""
		player = self.level.player

		scroll_width , scroll_height = 0 , 0
		level_width  , level_height = self.level.size[0] , self.level.size[1]
		screen_width , screen_height = self.screen_size[0] , self.screen_size[1]

		player_center = case_scale(player.right() - player.size.x /2 , player.bottom() - player.size.y/ 2 )

		# define maximum scroll width and height
		max_scroll_width , max_scroll_height =  level_width-screen_width , level_height - screen_height

		# calculating actual width and height of scrolling
		scroll_width +=   player_center[0] - ( screen_width/2 )
		#print ( str(screen_height/2)+"-"+str(player_center[1]))
		scroll_height +=  player_center[1] - (screen_height/2)
		# The screen can't scroll over the level right
		if scroll_width >= max_scroll_width:
			scroll_width = max_scroll_width
		# The screen can not scroll over the level left
		if scroll_width <= 0 :
			scroll_width = 0
		# The screen is not allowed to scrll below the level bottom
		if scroll_height >= max_scroll_height:
			scroll_height = max_scroll_height
		# The screen can not scroll above the level top
		if scroll_height <= 0 :
			scroll_height = 0 
			
		return (scroll_width, scroll_height)