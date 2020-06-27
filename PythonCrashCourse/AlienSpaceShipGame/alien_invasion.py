import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf

def run_game():
    #initialize pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_settings)

    #make a Ship
    ship = Ship(ai_settings, screen)

    #make a group to maintain bullet and aliens
    bullets = Group() #initialize empty group
    aliens = Group() #initialize empty group
    gf.create_alienfleet(ai_settings,screen,ship,aliens)

    #Start loop for run_game
    while True:
        #watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
            #Drawing screen with ship
        gf.update_screen(ai_settings,screen,ship, aliens, bullets)

run_game()
