#-*-coding:utf-8-*-
try:
	import sys
	from threading import Thread
	from physics.vector import Vector 
except ImportError as err:
	print ("Importation error at physics/gravity.py : {}".format(err))
	sys.exit(0)
"""threading interface for gravity simulation"""
class Gravity(Thread):
	def __init__(self,actor):
		Thread.__init__(self,actor)
		self.gravity = 9.8
		self.acceleration = Vector(0,self.gravity/10)
		self.actor = actor
		self.force = actor.mass * self.gravity

	def accelerate_actor_fall(self):
		self.actor.velocity = self.actor.velocity + self.acceleration

	def run():
		while actor.isAlive():
			if not (actor.object_is_below()):
				self.accelerate_actor_fall()
				self.actor.fall()
