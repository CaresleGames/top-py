import pygame, math
from pygame.locals import *

def check_collision(rect1 : pygame.Rect, rect2 : pygame.Rect) -> bool:
	if (
		rect1.x > rect2.x + rect2.width
		or rect1.x + rect1.width < rect2.x
		or rect1.y > rect2.y + rect2.height
		or rect1.y + rect1.height < rect2.y
	):
		return False
	return True


def calculate_angle(pos_x, pos_y) -> float:
	deg = math.atan2(pos_y, pos_x)
	# Multiply for -1 for rotate correct the image
	deg = math.degrees(deg) * -1
	return deg