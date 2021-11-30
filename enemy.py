import pygame
from pygame.locals import *
from base_object import BaseObject

class Enemy(BaseObject):
	def __init__(self, x, y, img_path: str) -> None:
		super().__init__(x, y, img_path)
		self.init_speed = 0.1
		self.speed = self.init_speed
		self.direction = pygame.Vector2(1, 1)

	def move(self, player):
		pos_x = self.position.x - player.position.x
		pos_y = self.position.y - player.position.y
		self.update_direction(pos_x, pos_y)
		self.position.x += self.speed * self.direction.x
		self.position.y += self.speed * self.direction.y

	def update_direction(self, x, y):
		if x > 0:
			self.direction.x = -1
		if x < 0:
			self.direction.x = 1
		if x == 0:
			self.direction.x = 0
		if y > 0:
			self.direction.y = -1
		if y < 0:
			self.direction.y = 1
		if y == 0:
			self.direction.y = 0