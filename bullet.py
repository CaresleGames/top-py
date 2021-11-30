import pygame, math
from pygame.locals import *
from base_object import BaseObject

class Bullet(BaseObject):
	def __init__(self, x, y, img_path: str) -> None:
		super().__init__(x, y, img_path)
		# The image that will rotate for prevent pixel's get weird
		self.original_img = self.image
		self.speed = 8
		self.angle = 0
		self.moving = False
		self.direction = pygame.Vector2(1, 0)

	def move(self) -> None:
		self.position.x += self.speed * math.cos(math.radians(self.angle))
		self.position.y += self.speed * math.sin(math.radians(self.angle))

	def rotate_image(self, angle) -> None:
		self.image = pygame.transform.rotate(self.original_img, angle)

		