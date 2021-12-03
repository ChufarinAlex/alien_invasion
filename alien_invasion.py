import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_function


def run_game():
    # Инициализирует модуль pygame, настройки и объект на экране.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Задается задний фон.
    bg_color = (230, 230, 230)

    # Создаётся корабль.
    ship = Ship(ai_settings, screen)
    # Создаётся группа для хранения снарядов.
    bullets = Group()

    # Старт главного цикла игры.
    while True:
        game_function.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        game_function.update_bullets(bullets)
        game_function.update_screen(ai_settings, screen, ship, bullets)


run_game()