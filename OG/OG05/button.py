import pygame
from typing import Tuple
from config import Config
# ======== Класс кнопки ========
class Button:
    def __init__(self, x: int, y: int, width: int, height: int,
                 text: str, color: Tuple[int, int, int],
                 hover_color: Tuple[int, int, int]):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.current_color = color
        self.font = pygame.font.SysFont(None, 36)

    def draw(self, screen: pygame.Surface) -> None:
        """Отрисовка кнопок."""
        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=12)
        pygame.draw.rect(screen, Config.COLORS['white'], self.rect, 3, border_radius=12)
        text_surf = self.font.render(self.text, True, Config.COLORS['white'])
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_hovered(self, pos: Tuple[int, int]) -> bool:
        """Проверка наведения курсора на кнопку."""
        is_hover = self.rect.collidepoint(pos)
        self.current_color = self.hover_color if is_hover else self.color
        return is_hover

