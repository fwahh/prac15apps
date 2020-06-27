import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a class to represent a single alien in the float"""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load the alien image and set rect coords
        #chill -> whine -> upset
        self.image = pygame.image.load('images/alien_wow.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    def check_edges(self):
        """Return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
            
    def update(self):
        """Move the alien right"""
        self.x += (self.ai_settings.fleet_direction *
            self.ai_settings.alien_speed_factor)
        self.rect.x = self.x

    def blitalien(self):
        """Draw alien at its current location"""
        self.screen.blit(self.image,self.rect)
