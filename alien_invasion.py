import pygame as pg
import settings as sett
import ship
import game_functions as game_func

def run_game():
    pg.init()
    
    ai_settings = sett.Settings()
    game_screen = pg.display.set_mode(
        (ai_settings.screen_wigth,ai_settings.screen_height))
    pg.display.set_caption('Alien Invasion')
    
    player_ship = ship.Ship(ai_settings, game_screen)
    
    # Starting the main loop of game.
    while True:
        
        game_func.check_events(player_ship)        
        player_ship.update()
        game_func.update_screen(ai_settings, game_screen, player_ship)

run_game()