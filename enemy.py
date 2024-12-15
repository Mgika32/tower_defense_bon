import pygame
from pygame.math import Vector2
from enemy_data import ENEMY_DATA
import constants as c
import math

class Enemy(pygame.sprite.Sprite):
  def __init__(self, enemy_type, waypoints, images):
      pygame.sprite.Sprite.__init__(self)
      self.waypoints = waypoints
      self.pos = Vector2(self.waypoints[0])
      self.target_waypoint = 1
      self.health = ENEMY_DATA.get(enemy_type)["health"]
      self.speed = ENEMY_DATA.get(enemy_type)["speed"]
      self.angle = 0
      
      # Animation setup
      self.sprite_sheet = images.get(enemy_type)
      self.animation_list = self.load_animations()
      self.frame_index = 0
      self.update_time = pygame.time.get_ticks()
      
      # Set initial image
      self.original_image = self.animation_list[self.frame_index]
      self.image = pygame.transform.rotate(self.original_image, self.angle)
      self.rect = self.image.get_rect()
      self.rect.center = self.pos
  def load_animations(self):
      animations = []
      sprite_width = self.sprite_sheet.get_height()  # Assuming square sprites
      sprite_count = self.sprite_sheet.get_width() // sprite_width
      
      for x in range(sprite_count):
          temp_img = self.sprite_sheet.subsurface(x * sprite_width, 0, sprite_width, sprite_width)
          animations.append(temp_img)
      return animations
  def update(self, world):
      self.move(world)
      self.animate()
      self.rotate()
      self.check_alive(world)
  def animate(self):
      ANIMATION_COOLDOWN = 100  # Milliseconds between frames
      current_time = pygame.time.get_ticks()
      
      if current_time - self.update_time >= ANIMATION_COOLDOWN:
          self.frame_index = (self.frame_index + 1) % len(self.animation_list)
          self.original_image = self.animation_list[self.frame_index]
          self.update_time = current_time
  def check_alive(self, world):
    if self.health <= 0:
      world.killed_enemies += 1
      world.money += c.KILL_REWARD      
      self.kill()