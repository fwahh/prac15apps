import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings
        #load the ship image and get its rect.
        self.image = pygame.image.load('images/spaceship2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen_rect
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

        #Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        #initialize movement flags
        self.moving_right = False
        self.moving_left = False

    def blitship(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """Update ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        # moving left is in a separate if block so that if players
        #move both left and right at the same time, the right key would not
        #have higher priority
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx
