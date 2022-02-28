import pygame

class Ship:
    
    def __init__(self, game_screen) -> None:
        self.game_screen = game_screen
        
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = game_screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 100
        
    def blitme(self) -> None:
        self.game_screen.blit(self.image, self.rect)