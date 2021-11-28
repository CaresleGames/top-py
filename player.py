import pygame
from pygame.locals import *
from base_object import BaseObject

class Player(BaseObject):

	def __init__(self, x, y, img_path: str, speed) -> None:
		super().__init__(x, y, img_path)
		self.speed = speed

	def move(self, keys, width, height) -> None:
		if keys[K_a] and self.position.x > 0:
			self.position.x -= self.speed
		if keys[K_d] and self.position.x + self.position.width < width:
			self.position.x += self.speed
		if keys[K_w] and self.position.y > 0:
			self.position.y -= self.speed
		if keys[K_s] and self.position.y + self.position.height < height:
			self.position.y += self.speed