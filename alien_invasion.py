import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as game_func

def run_game():
    pygame.init()
    
    ai_settings = Settings()
    game_screen = pygame.display.set_mode(
        (ai_settings.screen_wigth,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    
    player_ship = Ship(game_screen)
    
    # Starting the main loop of game.
    while True:
        
        game_func.check_events()
        
        # The screen is redrawn on each iteration
        game_screen.fill(ai_settings.background_color)
        
        player_ship.blitme() 
        
        # Display the last screen drawn.        
        pygame.display.flip()

run_game()