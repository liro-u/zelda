import sys
sys.path.append("./code")

import pygame
from settings import *
from level import Level

class Game:
	def __init__(self):
    
    #general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Zelda')
		self.clock = pygame.time.Clock()
	
		self.level = Level()

		# sound
		main_sound = pygame.mixer.Sound('audio/main.ogg')
		main_sound.play(loops = -1)
		main_sound.set_volume(0.2)
	
	def is_action_pressed(self,action_name,key):
		for key_name in action_name.value:
			if key == key_name:
				return True
		return False

	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if self.is_action_pressed(Action.TOGGLE_UI,event.key) and self.level.player.is_alive:
						self.level.toggle_menu()
				
				
			self.screen.fill(WATER_COLOR)
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)


if __name__ == '__main__':
	game = Game()
	game.run()
