import sys

import pygame

from settings import Settings
from ship import Ship

def check_events() -> None:
    '''Handles key presses and mouse events'''
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    

def update_screen(ai_settings:Settings, game_screen:pygame.Surface, player_ship:Ship) -> None:
    '''Refreshes screen images and displays a new screen'''
    game_screen.fill(ai_settings.background_color)
    player_ship.blitme()    
    pygame.display.flip()