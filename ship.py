import pygame as pg
import settings as sett

class Ship:
    
    def __init__(self, ai_settings:sett.Settings, game_screen:pg.Surface) -> None:
        self.game_screen = game_screen
        self.ai_settings = ai_settings
        
        self.image = pg.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = game_screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 100
        self.center = float(self.rect.centerx)
        
        self.moving_right = False
        self.moving_left = False
      
      
    def update(self) -> None:  
        """Updates the position of the ship depending on the flag"""
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
        # 'rect' only stores the integer part of a number
        self.rect.centerx = self.center
        
        
    def blitme(self) -> None:
        self.game_screen.blit(self.image, self.rect)