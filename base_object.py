import pygame
from pygame.locals import *

class BaseObject:

	def __init__(self, x, y, img_path: str) -> None:
		self.image : pygame.Surface = pygame.image.load("assets/" + img_path).convert_alpha()
		self.position : pygame.Rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())


	def draw(self, screen : pygame.Surface) -> None:
		screen.blit(self.image, self.position)