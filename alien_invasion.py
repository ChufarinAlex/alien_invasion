import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_function as gf
from scoreboard import Scoreboard


def run_game():
    # Инициализирует модуль pygame, настройки и объект на экране.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Статистика игры.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Задается задний фон.
    bg_color = (230, 230, 230)

    # Создаётся корабль.
    ship = Ship(ai_settings, screen)
    # Создаётся группа для хранения снарядов.
    bullets = Group()
    aliens = Group()

    # Создаётся флот пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Старт главного цикла игры.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, ship,
            aliens, bullets)

        if stats.game_active:
            if stats.game_active:
                ship.update()
                gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                                  bullets)
                gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                                 bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets)

run_game()