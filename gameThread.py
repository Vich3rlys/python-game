#-*-coding:utf-8-*-
#!/usr/bin/python 3.5.0
#written by vicherlys
try:
	from threading import Thread
except ImportError as err:
	print("Error during importation at \"gameThread.py\" :{}".format(err))
class GameThread(Thread):
	""" Class GameThread to store games action in a different thread """
	def __init__(self,mainAction):
		super.__init__(self)
		self.action = mainAction
	def run(self):
		#run the action using a thread passed in the declaration in a thread
		return self.action()
