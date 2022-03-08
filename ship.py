from select import select
import pygame

class Ship:
    
    def __init__(self, game_screen:pygame.Surface) -> None:
        self.game_screen = game_screen
        
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = game_screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 100
        
        self.moving_right = False
      
      
    def update(self) -> None:  
        """Updates the position of the ship depending on the flag"""
        if self.moving_right:
           self.rect.centerx += 1
       
        
    def blitme(self) -> None:
        self.game_screen.blit(self.image, self.rect)