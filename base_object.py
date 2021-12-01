import pygame
from pygame.locals import *

class BaseObject:

	def __init__(self, x, y, img_path: str) -> None:
		self.image : pygame.Surface = pygame.image.load("assets/" + img_path).convert_alpha()
		self.position : pygame.Rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())


	def draw(self, screen : pygame.Surface) -> None:
		screen.blit(self.image, self.position)

	def on_screen(self, width = 800, height = 600) -> bool:
		if (
			self.position.x >= 0 and self.position.x <= width
			and self.position.y >= 0 and self.position.y <= height
		):
			return True
		return False
		