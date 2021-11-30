import pygame, sys
from pygame.locals import *

from utils import calculate_angle
from player import Player
from bullet import Bullet

pygame.init()

WIDTH, HEIGHT = 800, 600
screen : pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Limited space")

clock : pygame.time.Clock = pygame.time.Clock()
FPS = 60

player = Player(25, 25, "16x16.png", 6)
bullet = Bullet(120, 120, "bullet.png")

def main():
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					player.reload()
					print("reload")

			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse = pygame.mouse.get_pressed()
				if mouse[0] and player.bullets < player.bullets_limit:
					# Position for calculate the angle
					pos_x = pygame.mouse.get_pos()[0] - player.position.x
					pos_y = pygame.mouse.get_pos()[1] - player.position.y
					deg = calculate_angle(pos_x, pos_y)
					# Multiply for -1 for get the correct angle
					bullet.angle = deg * -1
					bullet.moving = True
					
					bullet.position.x = player.position.x
					bullet.position.y = player.position.y
					
					bullet.rotate_image(deg)
					player.bullets += 1
			
		keys = pygame.key.get_pressed()
		player.move(keys, WIDTH, HEIGHT)
		
		if bullet.moving:
			bullet.move()
		
		# Draw
		screen.fill((0, 0, 0))
		player.draw(screen)
		bullet.draw(screen)
		pygame.display.update()


if __name__ == '__main__':
	main()