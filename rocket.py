import pygame
from ship import Ship
import game_function as gf

def run_game():
    """ Game Run Function """
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Rocket")

    ship = Ship(screen)
    bg_color = (33, 39, 122)

    while True:
        """ Main Loop """
        gf.check_event(ship)

        screen.fill(bg_color)
        ship.update()
        gf.update_screen(screen, ship)

run_game()