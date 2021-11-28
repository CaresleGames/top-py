import pygame, sys
from pygame.locals import *
from player import Player
from bullet import Bullet
pygame.init()


WIDTH, HEIGHT = 800, 600
screen : pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Limited space")

clock : pygame.time.Clock = pygame.time.Clock()
FPS = 60

player = Player(25, 25, "16x16.png", 6)
bullet = Bullet(-100, -100, "bullet.png")

def main():
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
		keys = pygame.key.get_pressed()
		player.move(keys, WIDTH, HEIGHT)
		screen.fill((0, 0, 0))
		player.draw(screen)
		pygame.display.update()


if __name__ == '__main__':
	main()