from pygame import Surface as sfc
def get_map(map_design):
	Mfile= open(map_design,'r')
	level_map = Mfile.read()
	Mfile.close()
	return level_map.splitlines()

def draw_surface(size,color):
	surface= sfc(size)
	surface.fill(color)
	return surface
	
def path_from_level(level,lvl_path_list):
	if level>0 and level<=len(lvl_path_list):
		return lvl_path_list[level-1]
	return -1

def obj_from_char(legend,char):
	for key,elt in legend.items():
		if char == key:
			return elt
	return False

"""
def RunNewThread(function):
	thread = gameThread(function)
	thread.run()
	thread.close()
"""