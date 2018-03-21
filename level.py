#-*-coding:utf-8-*-
try:
	import sys ,tiles.wall ,sprites.player

	from library          import get_map ,obj_from_char ,path_from_level
	from variables        import lvl_names ,lvl_path ,case_scale
	from physics.vector   import Vector
except ImportError as err:
	sys.stdout.write("Importation error at \"level.py\" : {}".format(err))
	sys.exit()

class Level():
	global Wall,Player
	Wall = tiles.wall.Wall
	Player = sprites.player.Player

	def __init__(self,lvl):
		self.map = get_map(path_from_level(lvl,lvl_path))
		if len(self.map) < 0 :
			sys.sdout.write(" Unknown level Error !!!")
			sys.exit(0)
		self.name = lvl_names[lvl-1]
		self.tiles = list()
		self.sprites = list()
		self.player  = None
		#level's legend containing all character's translation to class
		self.legend = {
          '#':Wall,
          '@':Player,
          ' ':None}
		# all map's row elements have to pass to the <obj_from_char> function who make them a class object
		map_row = lambda string : list(map(lambda char:obj_from_char(self.legend,char),string))

		self.map =  list(map(lambda string : map_row(string),self.map))
		self.size = case_scale(len(self.map[0]),len(self.map))

	def get(x,y):
		return self.map[y][x]

	def class_elements(self):
		for y,row in enumerate(self.map):
			for x,elt in enumerate(row):
				if elt == Wall :
					elt = elt((x,y))
					self.tiles.append(elt)
				elif elt == Player:
					elt = elt((x,y),self)
					self.sprites.append(elt)
					self.player = elt
				else :
					continue
				self.map[y][x] = elt

	def get_objects(self):
		return self.tiles

	def get_actors(self):
		return self.sprites

	def draw_actors(self,screen):
		for x in range(len(self.sprites)):
			self.sprites[x].draw(screen)

	def draw_environment(self,screen):
		for x in range(len(self.tiles)):
			self.tiles[x].draw(screen)
		
	def draw(self,screen):
		self.draw_environment(screen)
		self.draw_actors(screen)