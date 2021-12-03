class Settings():
    """Класс, хранящий все настройки игры."""

    def __init__(self):
        """Инициализирует игровые настройки."""
        # Настройки экрана.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройки корабля.
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Настройки снарядов.
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Настройки пришельцев.
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 5
        self.fleet_direction = 1
