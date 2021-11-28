import pygame
from pygame.locals import *
from base_object import BaseObject

class Bullet(BaseObject):
	def __init__(self, x, y, img_path: str) -> None:
		super().__init__(x, y, img_path)
		self.image_rotate = pygame.transform.rotate(self.image, 90)
		self.image_normal = self.image
		self.speed = 8
		self.direction = pygame.Vector2(1, 0)

	def move(self) -> None:
		self.position.x += self.speed * self.direction.x 
		self.position.y += self.speed * self.direction.y