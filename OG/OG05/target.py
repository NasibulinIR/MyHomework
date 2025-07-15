import random
import pygame
from config import Config
from typing import Tuple
# ======== Класс мишени ========
class Target:
    def __init__(self):
        self.radius = random.randint(Config.TARGET_MIN_RADIUS, Config.TARGET_MAX_RADIUS)
        self.x = random.randint(self.radius + 140, Config.SCREEN_WIDTH - self.radius)  # Сдвигаем мишень на 140 пикселей справа для исключения спауна мишени внутри инфопанели
        self.y = random.randint(self.radius, Config.SCREEN_HEIGHT - self.radius)
        self.speed_x = random.choice([-3, -2, 2, 3])
        self.speed_y = random.choice([-3, -2, 2, 3])
        self.points = self._calculate_points()

    def _calculate_points(self) -> int:
        """Расчет очков за уничтожение мишени (в зависимости от размера, чем меньше мишень, тем больше очков)."""
        return max(50 - self.radius, 10)

    def move(self) -> None:
        """Движение мишени"""
        self.x += self.speed_x
        self.y += self.speed_y
        self._handle_bounce()

    def _handle_bounce(self) -> None:
        """Отскок от границ экрана."""
        if self.x - 140 < self.radius or self.x > Config.SCREEN_WIDTH - self.radius: # Сдвиг на 140 пикселей для корре
            self.speed_x *= -1
        if self.y < self.radius or self.y > Config.SCREEN_HEIGHT - self.radius:
            self.speed_y *= -1

    def draw(self, screen: pygame.Surface) -> None:
        """Отрисовка мишени на экране."""
        pygame.draw.circle(screen, Config.COLORS['blue'], (self.x, self.y), self.radius)
        pygame.draw.circle(screen, Config.COLORS['black'], (self.x, self.y), self.radius, 1)
        pygame.draw.circle(screen, Config.COLORS['red'], (self.x, self.y), self.radius * 0.65)
        pygame.draw.circle(screen, Config.COLORS['black'], (self.x, self.y), self.radius * 0.65, 1)
        pygame.draw.circle(screen, Config.COLORS['yellow'], (self.x, self.y), self.radius * 0.3)
        pygame.draw.circle(screen, Config.COLORS['black'], (self.x, self.y), self.radius * 0.3, 1)

    def is_hit(self, pos: Tuple[int, int]) -> bool:
        """Проверка на попадание в мишень."""
        dx = self.x - pos[0]
        dy = self.y - pos[1]
        return dx * dx + dy * dy <= self.radius * self.radius

