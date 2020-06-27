import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien

#to hold main game functions to increase readability, note that some of the
#functions can't be called directly from this file because they have references
# to other files e.g. ship,settings and will only be callable from main file


def check_keydown_events(event,ai_settings, screen, ship, bullets):
    """Respond to key presses"""
    if event.key == pygame.K_RIGHT:
        #move ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        #create a bullet and add it to bullets group if it's within bulletlimit
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        #stop moving ship
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update images on screen and flip to the new screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitship()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Update position of bullets and get rid of old bullets"""
    bullets.update() #to update the y coord each loop

    #Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    #check for bullets that have hit aliens and get rid of both
    #collisions will be returned as a dict
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

    if len(aliens)==0:
        #destroy remaining bullets and create new fleet_direction
        bullets.empty()
        create_alienfleet(ai_settings,screen,ship,aliens)


def get_number_aliens_x(ai_settings, alien_width):
    """Determine number of aliens that fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x/(2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    """Determine the number of rows of aliens that fit on screen"""
    available_space_y = (ai_settings.screen_height -
        (3*alien_height) - ship_height)
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in a row """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width *alien_number
    alien.rect.x = alien.x
    alien.rect.y = int(0.5*alien.rect.height) + 2*alien.rect.height*row_number
    aliens.add(alien)

def create_alienfleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens"""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,
        alien.rect.height)
    #create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            #create an alien and define its x,y coord
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_alienfleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    """
    Check if fleet is at an edge, then
    Update position of all aliens in the fleet
    """
    check_alienfleet_edges(ai_settings,aliens)
    aliens.update()

    #look for alien-ship collisions
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)

    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    """Respond to ship being hit by aliens"""
    if stats.ships_left > 0:
        #decrement ships left
        stats.ships_left -= 1

        #empty list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #recenter ship and create new fleet
        create_alienfleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
    else:
        stats.game_active = False

        #Pause
        sleep(0.5)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Check if aliens reached bottom of screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break
