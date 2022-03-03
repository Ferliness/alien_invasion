import sys

import pygame

from settings import Settings
from ship import Ship

def check_events(player_ship:Ship) -> None:
    '''Handles key presses and mouse events'''
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_ship.rect.centerx += 1
    

def update_screen(ai_settings:Settings, game_screen:pygame.Surface, player_ship:Ship) -> None:
    '''Refreshes screen images and displays a new screen'''
    game_screen.fill(ai_settings.background_color)
    player_ship.blitme()    
    pygame.display.flip()