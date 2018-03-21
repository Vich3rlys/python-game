#-*-coding:utf-8-*-
try :
	from Interface import *
	from level import *
except ImportError as err:
	print("Importation error at main.py : {}".format(err))

def main():
	lvl = 1
	level = Level(lvl)
	interface = Interface(level)
	interface.run_game()

if __name__ == "__main__":
	main()