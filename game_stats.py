class GameStats():
    """Статистика для игры Alien Invasion."""

    def __init__(self, ai_settings):
        """Инициализация статистики."""
        self.ai_settings = ai_settings
        self.reset_stats()

        self.game_active = True

    def reset_stats(self):
        """Статистика, изменяющаяся во время игры."""
        self.ships_left = self.ai_settings.ship_limit