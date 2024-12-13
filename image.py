import pygame
import constants as c
#load images
map_image = pygame.image.load('levels/level.png').convert_alpha()
#turret spritesheets
turret_spritesheets = []
for x in range(1, c.TURRET_LEVELS + 1):
  turret_sheet = pygame.image.load(f'assets/images/turrets/turret_{x}.png').convert_alpha()
  turret_spritesheets.append(turret_sheet)
#individual turret image for mouse cursor
cursor_turret = pygame.image.load('assets/images/turrets/cursor_turret.png').convert_alpha()
#enemies
enemy_images = {
  "weak": pygame.image.load('assets/images/enemies/enemy_1.png').convert_alpha(),
  "medium": pygame.image.load('assets/images/enemies/enemy_2.png').convert_alpha(),
  "strong": pygame.image.load('assets/images/enemies/enemy_3.png').convert_alpha(),
  "elite": pygame.image.load('assets/images/enemies/enemy_4.png').convert_alpha()
}
#buttons
buy_turret_image = pygame.image.load('assets/images/buttons/buy_turret.png').convert_alpha()
cancel_image = pygame.image.load('assets/images/buttons/cancel.png').convert_alpha()
upgrade_turret_image = pygame.image.load('assets/images/buttons/upgrade_turret.png').convert_alpha()
begin_image = pygame.image.load('assets/images/buttons/begin.png').convert_alpha()
restart_image = pygame.image.load('assets/images/buttons/restart.png').convert_alpha()
fast_forward_image = pygame.image.load('assets/images/buttons/fast_forward.png').convert_alpha()
#gui
heart_image = pygame.image.load("assets/images/gui/heart.png").convert_alpha()
coin_image = pygame.image.load("assets/images/gui/coin.png").convert_alpha()
logo_image = pygame.image.load("assets/images/gui/logo.png").convert_alpha()

#load sounds
shot_fx = pygame.mixer.Sound('assets/audio/shot.wav')
shot_fx.set_volume(0.5)
