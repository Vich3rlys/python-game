"""Global variables used for the project "Undergound" """

#########################################################
#---------------------- Colors ------------------------#
#########################################################
white = (255,255,255)
black = 0x000
colors = [
    0xffffff,
    (63,63,63),
    (21,222,31),
    (179,48,15),
    (247,221,79)]	#list of available colors
wall_color = colors[0]
background_color  = colors[1]
player_color = colors[2]
lava_color = colors[3]
gold_color = colors[4]

#########################################################
#-----------------  Display settings  ------------------#
#########################################################
case = 20
case_scale   = lambda x,y: (x*case,y*case)

width= int(case*37.5)   #750px
height = int(case*17.5) #350px
screen_size = (width,height)

#########################################################
#---------------------  Images  ------------------------#
#########################################################
#maybe I should replace them with nice images later and resize images with pygame smoothscale
try:
	import sys
	from library import draw_surface
except ImportError as err:
	print("Importation error at variables.py :{}".format(err))
	sys.exit(0)
wall_image   = draw_surface(case_scale(  1 , 1  ),wall_color)
player_image = draw_surface(case_scale( 0.8,1.2 ),player_color)
gold_image   = draw_surface(case_scale( 0.5,0.5 ),gold_color)
lava_image   = draw_surface(case_scale(  1 , 1  ),lava_color)

#########################################################
#-------------------  Level related  -------------------#
#########################################################
file_ext = ".txt"
lvl_dir = "lvl_designs/"
#level's names list
lvl_names= ["start"]
#convert level name list to level path list
#lvl_path = map( lambda lvl_name: lvl_dir+lvl_name+file_ext, lvl_names)
lvl_path=list()
for x in range(len(lvl_names)):
	lvl_name = lvl_names[x]
	lvl_path.append(lvl_dir+lvl_name+file_ext)