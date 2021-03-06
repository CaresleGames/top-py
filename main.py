import pygame, sys
from pygame.locals import *
from typing import List

from utils import calculate_angle, check_collision
from player import Player
from bullet import Bullet
from enemy import Enemy

pygame.init()

WIDTH, HEIGHT = 800, 600
screen : pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top py")

clock : pygame.time.Clock = pygame.time.Clock()
FPS = 60

player = Player(WIDTH // 2 - 8, HEIGHT // 2 - 8, "16x16.png", 6)

# Bullets
bullets : List[Bullet] = []
last_bullet = 0

# Enemy
enemies : List[Enemy] = []
last_enemy = 0
# Timer
pygame.time.set_timer(pygame.USEREVENT, 1000)

# Font
font = pygame.font.Font("assets/KenneyPixelSquare.ttf", 16)

def main():
	run = True
	global last_bullet
	global last_enemy

	for n in range(0, 20):
		b = Bullet(-100, -100, "bullet.png")
		bullets.append(b)
	for n in range(0, 5):
		e = Enemy(-300, -300, "enemy.png")
		enemies.append(e)
	game_end = False
	
	score = 0

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
				if event.key == pygame.K_SPACE and game_end:
					player.restart()
					for enemy in enemies:
						enemy.restart()
					game_end = False
			
			if event.type == pygame.USEREVENT:
				if last_enemy < len(enemies) - 1:
					enemies[last_enemy].random_position(WIDTH, HEIGHT)
					last_enemy += 1

			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse = pygame.mouse.get_pressed()
				if mouse[0] and player.bullets < player.bullets_limit and player.is_alive:
					if last_bullet > len(bullets) - 1:
						last_bullet = 0
					
					# Position for calculate the angle
					pos_x = pygame.mouse.get_pos()[0] - player.position.x
					pos_y = pygame.mouse.get_pos()[1] - player.position.y
					deg = calculate_angle(pos_x, pos_y)
					
					# Multiply for -1 for get the correct angle
					bullets[last_bullet].angle = deg * -1
					bullets[last_bullet].moving = True
					
					# Change bullet position
					bullets[last_bullet].change_position(player.position)
					bullets[last_bullet].rotate_image(deg)
					
					player.bullets += 1
					last_bullet += 1
			
		keys = pygame.key.get_pressed()
		
		player.move(keys, WIDTH, HEIGHT)

		# Draw
		screen.fill((0, 0, 0))
		if player.is_alive:
			player.draw(screen)

			for enemy in enemies:
				if check_collision(enemy.position, player.position):
					player.is_alive = False
					game_end = True
				enemy.move(player)
				enemy.draw(screen)

		for bullet in bullets:
			if bullet.moving:
				# Check collision with enemies
				for enemy in enemies:
					if check_collision(enemy.position, bullet.position):
						enemy.increase_speed()
						enemy.send_out()
						score += 1
				bullet.move()

			if bullet.is_on_screen:
				bullet.draw(screen)

		if not game_end:
			score_text = font.render(f"Score: {score}", False, (255, 255, 255))
			screen.blit(score_text, (0, 0))
		else:
			text = font.render("Game Over", False, (255, 255, 255))
			screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

		pygame.display.update()


if __name__ == '__main__':
	main()