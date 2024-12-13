import pygame
import sys
from random import *
import constants as c
from pygame.math import Vector2
import math
from enemy_data import ENEMY_DATA
from world import World
import json
from turret import Turret
from turret_data import TURRET_DATA
from enemy import Enemy
from image import *
# Variable initialization
inv = {"a": 0, "b": 0, "artillerie": 0, "c": 0, "lance grenade": 0, "d": 0, "sorcier": 0, "cannonier": 0, "lance_pierre": 0, "archer": 0, "caserne": 0, "ralentisseur" : 0}
liste_item = {5: ["a", "b"], 4: ["artillerie", "c"], 3: ['lance grenade', "d"], 2: ['sorcier', 'cannonier'], 1: ['lance_pierre', 'archer', 'caserne']}
button_caisse_rect = pygame.Rect(50, 100, 100, 50)
button_epique_rect = pygame.Rect(250, 100, 100, 50)

pygame.init()

WIDTH, HEIGHT = 1050, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu avec Play et Gasha")
# Color palette
COLORS = {
    'background': (245, 245, 245),    # Light gray background
    'primary': (70, 130, 180),        # Steel blue for main elements
    'secondary': (255, 255, 255),     # White for contrast
    'text': (50, 50, 50),            # Dark gray for text
    'button': {
        'normal': (200, 200, 200),    # Light gray for buttons
        'hover': (180, 180, 180),     # Slightly darker for hover
        'border': (100, 100, 100)     # Dark gray for borders
    },
    'rarity': {
        1: (192, 192, 192),    # Silver for common
        2: (50, 205, 50),      # Lime green for uncommon
        3: (65, 105, 225),     # Royal blue for rare
        4: (148, 0, 211),      # Purple for epic
        5: (255, 215, 0)       # Gold for legendary
    }
}
# Load background image
background_img = pygame.image.load("assets/images/background/ton_image_de_fond.png")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Create fonts
font = pygame.font.Font(None, 50)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
# Button texts
play_text = font.render('Play', True, BLACK)
gasha_text = font.render('Gasha', True, BLACK)
retour_text = font.render('Retour', True, BLACK)
inv_text = font.render('Inventaire', True, BLACK)


# Button positions
play_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 100, 200, 50)
inventory_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 200, 200, 50)
gasha_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
button_retour_rect = pygame.Rect(50, 550, 100, 50)

def draw_button(rect, text):
    pygame.draw.rect(screen, GRAY, rect)
    screen.blit(text, (rect.x + (rect.width - text.get_width()) // 2, rect.y + (rect.height - text.get_height()) // 2))

def tirage(crate):
    tirage_proba = randint(1,100)
    sorti_etoile = 0
    if crate == 1:
        
        if tirage_proba <= 50:
            sorti_etoile = 1
        elif tirage_proba <= 80:
            sorti_etoile = 2
        elif tirage_proba <= 90:
            sorti_etoile = 3
        elif tirage_proba <= 96:
            sorti_etoile = 4 
        else: 
            sorti_etoile = 5
    else :
        if tirage_proba <= 30:
            sorti_etoile = 1
        elif tirage_proba <= 60:
            sorti_etoile = 2
        elif tirage_proba <= 75:
            sorti_etoile = 3
        elif tirage_proba <= 90:
            sorti_etoile = 4 
        else: 
            sorti_etoile = 5
    print(f"sorti_etoile = {sorti_etoile}")
    return sorti_etoile

def display_gacha(screen):
    # Background with gradient
    screen.fill((245, 245, 245))
    
    # Title
    title_font = pygame.font.Font(None, 60)
    title = title_font.render("Gacha Shop", True, (50, 50, 50))
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 50))
    
    # Crate buttons with better styling
    simple_crate = pygame.Rect(WIDTH//4 - 100, HEIGHT//2 - 100, 200, 200)
    epic_crate = pygame.Rect(3*WIDTH//4 - 100, HEIGHT//2 - 100, 200, 200)
    
    # Draw crates with shadows
    pygame.draw.rect(screen, (180, 180, 180), simple_crate.move(5, 5), border_radius=20)
    pygame.draw.rect(screen, (220, 100, 100), simple_crate, border_radius=20)
    pygame.draw.rect(screen, (180, 180, 180), epic_crate.move(5, 5), border_radius=20)
    pygame.draw.rect(screen, (100, 150, 220), epic_crate, border_radius=20)
    
    # Crate labels
    crate_font = pygame.font.Font(None, 40)
    simple_text = crate_font.render("Simple Crate", True, (255, 255, 255))
    epic_text = crate_font.render("Epic Crate", True, (255, 255, 255))
    
    screen.blit(simple_text, (simple_crate.centerx - simple_text.get_width()//2, 
                             simple_crate.centery - simple_text.get_height()//2))
    screen.blit(epic_text, (epic_crate.centerx - epic_text.get_width()//2, 
                           epic_crate.centery - epic_text.get_height()//2))
    
    # Return button
    button_retour_rect = pygame.Rect(50, 550, 120, 50)
    pygame.draw.rect(screen, (200, 200, 200), button_retour_rect, border_radius=15)
    pygame.draw.rect(screen, (100, 100, 100), button_retour_rect, 2, border_radius=15)
    retour_text = font.render("Return", True, (50, 50, 50))
    screen.blit(retour_text, (button_retour_rect.centerx - retour_text.get_width()//2,
                             button_retour_rect.centery - retour_text.get_height()//2))
    
    return simple_crate, epic_crate, button_retour_rect

def display_reward(screen, item, rarity):
    # Animated reward display
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 128))
    screen.blit(overlay, (0, 0))
    
    # Rarity colors
    rarity_colors = {
        1: (200, 200, 200),  # Common
        2: (100, 200, 100),  # Uncommon
        3: (100, 100, 200),  # Rare
        4: (200, 100, 200),  # Epic
        5: (255, 215, 0)     # Legendary
    }
    
    # Reward box
    reward_rect = pygame.Rect(WIDTH//2 - 150, HEIGHT//2 - 100, 300, 200)
    pygame.draw.rect(screen, rarity_colors[rarity], reward_rect, border_radius=20)
    pygame.draw.rect(screen, (255, 255, 255), reward_rect, 4, border_radius=20)
    
    # Item text
    reward_font = pygame.font.Font(None, 50)
    item_text = reward_font.render(item, True, (255, 255, 255))
    screen.blit(item_text, (reward_rect.centerx - item_text.get_width()//2,
                           reward_rect.centery - item_text.get_height()//2))


def choix_item(sortie_etoile,liste_item,inv):
    item = liste_item[sortie_etoile] [randint(0,len(liste_item[sortie_etoile])-1)]
    if item in inv:
        print(f"tu as eu {item} ")
        inv[item] += 1
        pygame.display.flip()
        pygame.display.flip()
        return item
    
# Add this constant at the start
RETURN_BUTTON_RECT_INV = pygame.Rect(20, 20, 120, 50)

def display_inventory(screen, inv):
    # Background
    screen.fill((245, 245, 245))  # Light gray background
    
    # Return button in top left
    pygame.draw.rect(screen, (200, 200, 200), RETURN_BUTTON_RECT_INV, border_radius=15)
    pygame.draw.rect(screen, (100, 100, 100), RETURN_BUTTON_RECT_INV, 2, border_radius=15)
    retour_text = font.render("Return", True, (50, 50, 50))
    screen.blit(retour_text, (RETURN_BUTTON_RECT_INV.centerx - retour_text.get_width()//2,
                             RETURN_BUTTON_RECT_INV.centery - retour_text.get_height()//2))
    
    # Title
    title_font = pygame.font.Font(None, 60)
    title = title_font.render("Inventaire", True, (50, 50, 50))
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 50))
    
    # Item display
    item_font = pygame.font.Font(None, 40)
    start_x = 100
    start_y = 150
    spacing_y = 50
    
    for i, (item, quantity) in enumerate(inv.items()):
        if quantity > 0:
            # Item background
            item_rect = pygame.Rect(start_x, start_y + i*spacing_y, 400, 40)
            pygame.draw.rect(screen, (255, 255, 255), item_rect, border_radius=10)
            pygame.draw.rect(screen, (100, 100, 100), item_rect, 2, border_radius=10)
            
            # Item name
            item_text = item_font.render(f"{item}: {quantity}", True, (50, 50, 50))
            screen.blit(item_text, (start_x + 20, start_y + i*spacing_y + 5))

    return RETURN_BUTTON_RECT_INV



#classes : 

class Button():
  def __init__(self, x, y, image, single_click):
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    self.clicked = False
    self.single_click = single_click

  def draw(self, surface):
    action = False
    #get mouse position
    pos = pygame.mouse.get_pos()

    #check mouseover and clicked conditions
    if self.rect.collidepoint(pos):
      if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        action = True
        #if button is a single click type, then set clicked to True
        if self.single_click:
          self.clicked = True

    if pygame.mouse.get_pressed()[0] == 0:
      self.clicked = False

    #draw button on screen
    surface.blit(self.image, self.rect)

    return action

#game variables
game_over = False
game_outcome = 0 # -1 is loss & 1 is win
level_started = False
last_enemy_spawn = pygame.time.get_ticks()
placing_turrets = False
selected_turret = None


#load json data
with open('levels/level.tmj') as file:
  world_data = json.load(file)

#police pour afficher le texte
text_font = pygame.font.SysFont("Consolas", 24, bold = True)
large_font = pygame.font.SysFont("Consolas", 36)

#fonction poru afficher le texte a l'ecran
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

def display_data():
  pygame.draw.rect(screen, "maroon", (c.SCREEN_WIDTH, 0, c.SIDE_PANEL, c.SCREEN_HEIGHT))
  pygame.draw.rect(screen, "grey0", (c.SCREEN_WIDTH, 0, c.SIDE_PANEL, 400), 2)
  screen.blit(logo_image, (c.SCREEN_WIDTH, 400))
  #affiche les données 
  draw_text("LEVEL: " + str(world.level), text_font, "grey100", c.SCREEN_WIDTH + 10, 10)
  screen.blit(heart_image, (c.SCREEN_WIDTH + 10, 35))
  draw_text(str(world.health), text_font, "grey100", c.SCREEN_WIDTH + 50, 40)
  screen.blit(coin_image, (c.SCREEN_WIDTH + 10, 65))
  draw_text(str(world.money), text_font, "grey100", c.SCREEN_WIDTH + 50, 70)
  

def create_turret(mouse_pos):
  mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
  mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
  #calcule les sequence pour les tiles de la map 
  mouse_tile_num = (mouse_tile_y * c.COLS) + mouse_tile_x
  #check if that tile is grass
  if world.tile_map[mouse_tile_num] == 7:
    #regarde si il n'y a pas deja une tourelle 
    space_is_free = True
    for turret in turret_group:
      if (mouse_tile_x, mouse_tile_y) == (turret.tile_x, turret.tile_y):
        space_is_free = False
    #si l'espace est libre alors on cree la tourelle
    if space_is_free == True:
      new_turret = Turret(turret_spritesheets, mouse_tile_x, mouse_tile_y, shot_fx)
      turret_group.add(new_turret)
      #paye la tourelle
      world.money -= c.BUY_COST

def select_turret(mouse_pos):
  mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
  mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
  for turret in turret_group:
    if (mouse_tile_x, mouse_tile_y) == (turret.tile_x, turret.tile_y):
      return turret

def clear_selection():
  for turret in turret_group:
    turret.selected = False

#crée le monde
world = World(world_data, map_image)
world.process_data()
world.process_enemies()

#crée les groupes
enemy_group = pygame.sprite.Group()
turret_group = pygame.sprite.Group()

#crée les boutons
turret_button = Button(c.SCREEN_WIDTH + 30, 120, buy_turret_image, True)
cancel_button = Button(c.SCREEN_WIDTH + 50, 180, cancel_image, True)
upgrade_button = Button(c.SCREEN_WIDTH + 5, 180, upgrade_turret_image, True)
begin_button = Button(c.SCREEN_WIDTH + 60, 300, begin_image, True)
restart_button = Button(310, 300, restart_image, True)
fast_forward_button = Button(c.SCREEN_WIDTH + 50, 300, fast_forward_image, False)

running = True
inmenu = True
ingasha = False
in_play = False
in_inv = False

while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if inmenu : 
              if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    print("Play Button Pressed!")
                    inmenu = False
                    in_play = True
                if gasha_button_rect.collidepoint(event.pos):
                    print("Gasha Button Pressed!")
                    inmenu = False
                    ingasha = True
                if inventory_button_rect.collidepoint(event.pos):
                   print("Inv button pressed!")
                   in_inv = True

            if in_inv:
              if event.type == pygame.MOUSEBUTTONDOWN:
                if button_retour_rect.collidepoint(event.pos):
                  print("Retour Button Pressed!")
                  in_inv = False
                  inmenu = True
               
    if inmenu:
        screen.blit(background_img, (0, 0))
        draw_button(play_button_rect, play_text)
        draw_button(gasha_button_rect, gasha_text)
        draw_button(inventory_button_rect, inv_text) 

    if in_inv:
      button_retour_rect = display_inventory(screen, inv)
      if event.type == pygame.MOUSEBUTTONDOWN:
          if RETURN_BUTTON_RECT_INV.collidepoint(event.pos):
              in_inv = False
              inmenu = True

      
    elif ingasha:
        simple_crate, epic_crate, button_retour_rect = display_gacha(screen)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if simple_crate.collidepoint(event.pos):
                crate = 1
                etoile = tirage(crate)
                item = choix_item(etoile, liste_item, inv)
                display_reward(screen, item, etoile)
                pygame.display.flip()
                pygame.time.delay(2000)
            elif epic_crate.collidepoint(event.pos):
                crate = 2
                etoile = tirage(crate)
                item = choix_item(etoile, liste_item, inv)
                display_reward(screen, item, etoile)
                pygame.display.flip()
                pygame.time.delay(2000)
            elif button_retour_rect.collidepoint(event.pos):
                ingasha = False
                inmenu = True
    elif in_play:
       if game_over == False:
        #regarde si le joueur a perdu
        if world.health <= 0:
          game_over = True
          game_outcome = -1 #loss
        #regarde si le joueur a gagne
        if world.level > c.TOTAL_LEVELS:
          game_over = True
          game_outcome = 1 #win

        #update groups
        enemy_group.update(world)
        turret_group.update(enemy_group, world)

        #surligne la tourelle selectionnée
        if selected_turret:
          selected_turret.selected = True
        #dessine le level
        world.draw(screen)
        #dessine les groups
        enemy_group.draw(screen)
        for turret in turret_group:
          turret.draw(screen)
        display_data()
        if game_over == False:
          #regarde si le niveau a été démarré ou non
          if level_started == False:
            if begin_button.draw(screen):
              level_started = True
          else:
            #deplacement rapide 
            world.game_speed = 1
            if fast_forward_button.draw(screen):
              world.game_speed = 2
            #spawn enemies
            if pygame.time.get_ticks() - last_enemy_spawn > c.SPAWN_COOLDOWN:
              if world.spawned_enemies < len(world.enemy_list):
                enemy_type = world.enemy_list[world.spawned_enemies]
                enemy = Enemy(enemy_type, world.waypoints, enemy_images)
                enemy_group.add(enemy)
                world.spawned_enemies += 1
                last_enemy_spawn = pygame.time.get_ticks()
          #regarde si le niveau est fini
          if world.check_level_complete() == True:
            world.money += c.LEVEL_COMPLETE_REWARD
            world.level += 1
            level_started = False
            last_enemy_spawn = pygame.time.get_ticks()
            world.reset_level()
            world.process_enemies()
          draw_text(str(c.BUY_COST), text_font, "grey100", c.SCREEN_WIDTH + 215, 135)
          screen.blit(coin_image, (c.SCREEN_WIDTH + 260, 130))
          if turret_button.draw(screen):
            placing_turrets = True
          #si tu places des tourelles alors montre le bouton annuler
          if placing_turrets == True:
            #affiche le curseur tourelle 
            cursor_rect = cursor_turret.get_rect()
            cursor_pos = pygame.mouse.get_pos()
            cursor_rect.center = cursor_pos
            if cursor_pos[0] <= c.SCREEN_WIDTH:
              screen.blit(cursor_turret, cursor_rect)
            if cancel_button.draw(screen):
              placing_turrets = False
          #si il y a une tourelle selectionnée alors montre le bouton annuler
          if selected_turret:
            #if a turret can be upgraded then show the upgrade button
            if selected_turret.upgrade_level < c.TURRET_LEVELS:
              #montre le prix et l'affiche
              draw_text(str(c.UPGRADE_COST), text_font, "grey100", c.SCREEN_WIDTH + 215, 195)
              screen.blit(coin_image, (c.SCREEN_WIDTH + 260, 190))
              if upgrade_button.draw(screen):
                if world.money >= c.UPGRADE_COST:
                  selected_turret.upgrade()
                  world.money -= c.UPGRADE_COST
        else:
          pygame.draw.rect(screen, "dodgerblue", (200, 200, 400, 200), border_radius = 30)
          if game_outcome == -1:
            draw_text("GAME OVER", large_font, "grey0", 310, 230)
          elif game_outcome == 1:
            draw_text("YOU WIN!", large_font, "grey0", 315, 230)
          #restart
          if restart_button.draw(screen):
            game_over = False
            level_started = False
            placing_turrets = False
            selected_turret = None
            last_enemy_spawn = pygame.time.get_ticks()
            world = World(world_data, map_image)
            world.process_data()
            world.process_enemies()
            #empty groups
            enemy_group.empty()
            turret_group.empty()
        #event handler
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            #regarde si la souris est dans la page 
            if mouse_pos[0] < c.SCREEN_WIDTH and mouse_pos[1] < c.SCREEN_HEIGHT:
              #clear les tourelles selectionnée
              selected_turret = None
              clear_selection()
              if placing_turrets == True:
                #regarde si tu as la thune pour acheter une tourelle
                if world.money >= c.BUY_COST:
                  create_turret(mouse_pos)
              else:
                selected_turret = select_turret(mouse_pos)
        pygame.display.flip()

    pygame.display.update()

pygame.quit()

# Add this at the start with other constants
RETURN_BUTTON_RECT = pygame.Rect(WIDTH - 150, 20, 120, 50)

def draw_return_button(screen):
    pygame.draw.rect(screen, (200, 200, 200), RETURN_BUTTON_RECT, border_radius=15)
    pygame.draw.rect(screen, (100, 100, 100), RETURN_BUTTON_RECT, 2, border_radius=15)
    retour_text = font.render("Return", True, (50, 50, 50))
    screen.blit(retour_text, (RETURN_BUTTON_RECT.centerx - retour_text.get_width()//2,
                             RETURN_BUTTON_RECT.centery - retour_text.get_height()//2))
