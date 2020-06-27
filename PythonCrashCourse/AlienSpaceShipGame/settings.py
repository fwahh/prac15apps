#A file to hold defined settings for Alien Invasion game

class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game settings"""
        #screen Settings
        self.screen_width = 1440
        self.screen_height = 800
        self.bg_color = (26, 38, 110)

        #ship settings
        self.ship_speed_factor = 1.5

        #bullet settings
        self.bullet_speed_factor = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (87, 227, 79)
        self.bullets_allowed = 3

        #alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 #1 denotes right, -1 denotes left

        #game stats Settings
        self.ship_limit = 3
