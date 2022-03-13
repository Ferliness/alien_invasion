import sys
import pygame
from settings import Settings
from ship import Ship

def check_keydown_events(event:pygame.event, player_ship:Ship) -> None:
    if event.key == pygame.K_RIGHT:
        player_ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        player_ship.moving_left = True


def check_keyup_events(event:pygame.event, player_ship:Ship) -> None:
    if event.key == pygame.K_RIGHT:
        player_ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        player_ship.moving_left = False
        

def check_events(player_ship:Ship) -> None:
    '''Handles key presses and mouse events'''
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:            
            check_keydown_events(event, player_ship)
        
        elif event.type == pygame.KEYUP:            
            check_keyup_events(event, player_ship)


def update_screen(ai_settings:Settings, game_screen:pygame.Surface, player_ship:Ship) -> None:
    '''Refreshes screen images and displays a new screen'''
    game_screen.fill(ai_settings.background_color)
    player_ship.blitme()    
    pygame.display.flip()