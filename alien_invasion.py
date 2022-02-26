import sys

import pygame

def run_game():
    pygame.init()
    game_screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('Alien Invasion')
    
    background_color =  (230, 230, 230)
    
    # Starting the main loop of game.
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # The screen is redrawn on each iteration
        game_screen.fill(background_color)
        
        # Display the last screen drawn.        
        pygame.display.flip()

run_game()