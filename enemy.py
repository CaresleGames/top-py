import pygame, random
from pygame.locals import *
from base_object import BaseObject

class Enemy(BaseObject):
	def __init__(self, x, y, img_path: str) -> None:
		super().__init__(x, y, img_path)
		self.init_speed = 2
		self.speed = self.init_speed
		self.direction = pygame.Vector2(1, 1)
		self.is_alive = True

	def move(self, player):
		pos_x = player.position.x - self.position.x
		pos_y = player.position.y - self.position.y
		self.update_direction(pos_x, pos_y)
		
		self.position.x += self.speed * self.direction.x
		self.position.y += self.speed * self.direction.y

	def update_direction(self, x, y):
		if x > 10:
			self.direction.x = 1
		elif x < -10:
			self.direction.x = -1
		else:
			self.direction.x = 0

		if y > 10:
			self.direction.y = 1
		elif y < -10:
			self.direction.y = -1
		else:
			self.direction.y = 0


	# Send the enemy outside of the screen viewports
	def send_out(self):
		self.position.x = -200
		self.position.y = -200
	
	# Set a new random position between x and y
	def random_position(self, x=800, y=600):
		self.position.x = random.randrange(0, x)
		self.position.y = random.randrange(0, y)

		if self.position.y > y // 2:
			self.position.y = y + 50
		else:
			self.position.y = 0 - 50


	def increase_speed(self):
		self.speed += 0.25

	def restart(self):
		self.speed = self.init_speed
		self.random_position()