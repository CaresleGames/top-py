import pygame
from pygame.locals import *
from base_object import BaseObject

class Bullet(BaseObject):
	def __init__(self, x, y, img_path: str) -> None:
		super().__init__(x, y, img_path)
		# The image that will rotate for prevent pixel's get weird
		self.original_img = self.image
		self.speed = 8
		self.direction = pygame.Vector2(1, 0)

	def move(self) -> None:
		self.position.x += self.speed * self.direction.x 
		self.position.y += self.speed * self.direction.y

	def rotate_image(self, angle) -> None:
		self.image = pygame.transform.rotate(self.original_img, angle)
		