import pygame
import constants as c

def load_enemy_images():
    # Load the scorpion spritesheet
    scorpion_spritesheet = pygame.image.load('assets/images/enemies/Scorpion.png').convert_alpha()
    
    # Create a dictionary to store different enemy types
    enemy_images = {
        "weak": scorpion_spritesheet,
        "medium": scorpion_spritesheet,
        "strong": scorpion_spritesheet,
        "elite": scorpion_spritesheet
    }
    return enemy_images
