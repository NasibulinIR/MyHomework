import pygame
import sys
from typing import List, Tuple
from config import Config, GameState
from target import Target
from button import Button

# ======== Основной класс игры ========
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
        pygame.display.set_caption("Стрелковый Тир")

        # Игровые ресурсы
        self._load_resources()

        # Игровое состояние
        self._init_game_state()

        # Создание UI элементов
        self._setup_ui()

    def _load_resources(self) -> None:
        """Загрузка игровых ресурсов."""
        try:
            self.background = pygame.transform.scale(
                pygame.image.load("img/background.jpg"),
                (Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT)
            )
            self.shot_sound = pygame.mixer.Sound("snd/missed.wav")
            self.hit_sound = pygame.mixer.Sound("snd/hit.wav")
        except Exception as e:
            print(f"Ошибка загрузки ресурсов: {e}")
            # Создаем заглушки
            self.background = pygame.Surface((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
            self.background.fill(Config.COLORS['red'])
            self.shot_sound = pygame.mixer.Sound(buffer=bytearray([0] * 44))
            self.hit_sound = pygame.mixer.Sound(buffer=bytearray([0] * 44))

        # Шрифты
        self.title_font = pygame.font.SysFont("arial", 64, bold=True)
        self.score_font = pygame.font.SysFont("arial", 22)
        self.info_font = pygame.font.SysFont("arial", 24)

    def _init_game_state(self) -> None:
        """Инициализация состояния игры."""
        self.score = 0
        self.misses = 0
        self.level = 1
        self.targets: List[Target] = []
        self.game_state = GameState.MENU
        pygame.mouse.set_visible(True)

    def _setup_ui(self) -> None:
        """Создание интерфейса."""
        button_x = Config.SCREEN_WIDTH // 2 - 110 # Отцентровка кнопок по оси X
        self.buttons = {
            'start': Button(button_x, Config.SCREEN_HEIGHT // 2, 200, 50,
                            "СТАРТ ИГРЫ", Config.COLORS['green'], (40, 180, 70)),
            'exit': Button(button_x, Config.SCREEN_HEIGHT // 2 + 80, 200, 50,
                           "ВЫХОД", Config.COLORS['red'], (180, 40, 50)),
            'menu': Button(button_x, Config.SCREEN_HEIGHT // 2 + 80, 200, 50,
                           "В МЕНЮ", Config.COLORS['blue'], (40, 100, 180)),
            'restart': Button(button_x, Config.SCREEN_HEIGHT // 2 + 160, 200, 50,
                              "СЫГРАТЬ ЕЩЁ", Config.COLORS['green'], (40, 180, 70))
        }

    def spawn_target(self) -> None:
        """Создает мишени."""
        self.targets.append(Target())

    def start_game(self) -> None:
        """Начало новой игры."""
        self._init_game_state()
        for _ in range(Config.INITIAL_TARGETS):
            self.spawn_target()
        self.game_state = GameState.PLAYING
        pygame.mouse.set_visible(False)

    def draw_sight(self, pos: Tuple[int, int]) -> None:
        """Отрисовка прицела."""
        x, y = pos
        pygame.draw.line(self.screen, Config.COLORS['green'], (x - 20, y), (x + 20, y), 2)
        pygame.draw.line(self.screen, Config.COLORS['green'], (x, y - 20), (x, y + 20), 2)
        pygame.draw.circle(self.screen, Config.COLORS['green'], (x + 1, y + 1), 10, 1)

    def _handle_playing_events(self, event: pygame.event.Event) -> None:
        """Обработка событий игрового режима."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            hit = any(
                target.is_hit(mouse_pos)
                for target in self.targets[:]
            )

            if hit:
                self._handle_hit(mouse_pos)
            else:
                self._handle_miss()

            # Проверка окончания игры
            if self.misses >= Config.MAX_MISSES:
                self.game_state = GameState.GAME_OVER
                pygame.mouse.set_visible(True)

    def _handle_hit(self, mouse_pos: Tuple[int, int]) -> None:
        """Обработка попаданий по мишени."""
        self.hit_sound.play()
        for target in self.targets[:]:
            if target.is_hit(mouse_pos):
                self.score += target.points
                self.targets.remove(target)
                self.spawn_target()  # Заменяем уничтоженную мишень
                break

    def _handle_miss(self) -> None:
        """Обработка промахов."""
        self.misses += 1
        self.shot_sound.play()

    def _handle_menu_events(self, event: pygame.event.Event) -> None:
        """Обработка событий меню."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.buttons['start'].is_hovered(mouse_pos):
                self.start_game()
            elif self.buttons['exit'].is_hovered(mouse_pos):
                pygame.quit()
                sys.exit()

    def _handle_game_over_events(self, event: pygame.event.Event) -> None:
        """Обработка события экрана при состоянии окончания игры."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.buttons['menu'].is_hovered(mouse_pos):
                self.game_state = GameState.MENU
            elif self.buttons['restart'].is_hovered(mouse_pos):
                self.start_game()

    def _update_game(self) -> None:
        """Обновляет состояние игры."""
        if self.game_state != GameState.PLAYING:
            return

        # Обновление мишеней
        for target in self.targets:
            target.move()

        # Проверка повышения уровня
        if self.score > self.level * Config.LEVEL_UP_SCORE:
            self.level += 1
            # Увеличиваем сложность
            for target in self.targets:
                target.speed_x = min(target.speed_x * 1.3, Config.TARGET_MAX_SPEED)
                target.speed_y = min(target.speed_y * 1.3, Config.TARGET_MAX_SPEED)

    def _draw_playing_ui(self) -> None:
        """Отрисовка интерфейса игрового режима."""
        # Мишени
        for target in self.targets:
            target.draw(self.screen)

        # Прицел
        self.draw_sight(pygame.mouse.get_pos())

        # Статистика
        score_text = self.score_font.render(f"Очки: {self.score}", True, Config.COLORS['green'])
        level_text = self.score_font.render(f"Уровень: {self.level}", True, Config.COLORS['yellow'])
        misses_text = self.score_font.render(f"Промахи: {self.misses}/{Config.MAX_MISSES}",
                                             True, Config.COLORS['red'])

        self.screen.blit(score_text, (20, 20))
        self.screen.blit(level_text, (20, 60))
        self.screen.blit(misses_text, (20, 100))

    def _draw_menu_ui(self) -> None:
        """Отрисовка меню."""
        # Заголовок
        title_shadow = self.title_font.render("СТРЕЛКОВЫЙ ТИР", True, Config.COLORS['black'])
        title_text = self.title_font.render("СТРЕЛКОВЫЙ ТИР", True, Config.COLORS['green'])
        self.screen.blit(title_shadow, (Config.SCREEN_WIDTH // 2 - title_shadow.get_width() // 2 + 5, 103))
        self.screen.blit(title_text, (Config.SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))

        # Инструкция
        instruction = self.info_font.render(
            "Метко сбивайте мишени, чтобы увеличить свой счет, промахнувшись 5 раз, игра завершается",
            True, Config.COLORS['yellow']
        )
        self.screen.blit(instruction,
                         (Config.SCREEN_WIDTH // 2 - instruction.get_width() // 2, 200))

        # Кнопки
        self.buttons['start'].draw(self.screen)
        self.buttons['exit'].draw(self.screen)

    def _draw_game_over_ui(self) -> None:
        """Отрисовка интерфейс экрана окончания игры."""
        # Заголовок
        title = self.title_font.render("ИГРА ОКОНЧЕНА", True, Config.COLORS['red'])
        self.screen.blit(title, (Config.SCREEN_WIDTH // 2 - title.get_width() // 2, 100))

        # Статистика
        score_text = self.score_font.render(f"Ваш счёт:            {self.score}", True, Config.COLORS['purple'])
        level_text = self.score_font.render(f"Текущий уровень: {self.level}", True,
                                            Config.COLORS['dark_green'])

        self.screen.blit(score_text, (Config.SCREEN_WIDTH // 2 - score_text.get_width() // 2, 200))
        self.screen.blit(level_text, (Config.SCREEN_WIDTH // 2 - level_text.get_width() // 2, 250))

        # Кнопки
        self.buttons['menu'].draw(self.screen)
        self.buttons['restart'].draw(self.screen)

    def run(self) -> None:
        """Главный игровой цикл."""
        clock = pygame.time.Clock()

        while True:
            mouse_pos = pygame.mouse.get_pos()

            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Обработка событий по состоянию игры
                if self.game_state == GameState.PLAYING:
                    self._handle_playing_events(event)
                elif self.game_state == GameState.MENU:
                    self._handle_menu_events(event)
                elif self.game_state == GameState.GAME_OVER:
                    self._handle_game_over_events(event)

            # Обновление состояния игры
            self._update_game()

            # Отрисовка фона
            self.screen.blit(self.background, (0, 0))

            # Отрисовка инфопанели (слева)
            if self.game_state == GameState.PLAYING:
                for x in range(0, 140):
                    pygame.draw.line(self.screen, (30, 40, 60), (x, 0), (x, Config.SCREEN_HEIGHT), 1)
                    pygame.draw.line(self.screen, Config.COLORS['black'],
                                     (139, 0), (139, Config.SCREEN_HEIGHT), 2)

            # Отрисовка UI по состоянию игры
            if self.game_state == GameState.PLAYING:
                self._draw_playing_ui()
            elif self.game_state == GameState.MENU:
                self._draw_menu_ui()
            elif self.game_state == GameState.GAME_OVER:
                self._draw_game_over_ui()

            # Обновление кнопок (затемнение при наведении)
            if self.game_state == GameState.MENU:
                for btn in ['start', 'exit']:
                    self.buttons[btn].is_hovered(mouse_pos)
            elif self.game_state == GameState.GAME_OVER:
                for btn in ['menu', 'restart']:
                    self.buttons[btn].is_hovered(mouse_pos)

            pygame.display.flip()
            clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()