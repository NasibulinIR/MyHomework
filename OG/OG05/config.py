from enum import Enum, auto
# ======== Конфигурация и константы ========
class Config:
    # Размеры экрана
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 768

    # Цвета
    COLORS = {
        'white': (255, 255, 255),
        'red': (255, 50, 50),
        'green': (10, 255, 0),
        'blue': (50, 100, 255),
        'yellow': (255, 255, 0),
        'black': (0, 0, 0),
        'purple': (128, 0, 128),
        'dark_green': (1, 80, 32)
    }

    # Параметры мишеней
    TARGET_MIN_RADIUS = 15 # Минимальный радиус мишени
    TARGET_MAX_RADIUS = 40 # Максимальный радиус мишени
    TARGET_MIN_SPEED = 2 # Минимальная скорость мишени
    TARGET_MAX_SPEED = 12 # Максимальная скорость мишени

    # Игровые параметры
    MAX_MISSES = 5 # Максимальное количество промахов
    LEVEL_UP_SCORE = 500 # Количество очков для повышения уровня
    INITIAL_TARGETS = 5 # Количество мишеней в игре


# ======== Вспомогательные типы ========
class GameState(Enum):
    MENU = auto()
    PLAYING = auto()
    GAME_OVER = auto()

