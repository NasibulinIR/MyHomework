import pygame
import random

pygame.init()

# Параметры игры
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
PLAYER_SPEED = 6
BULLET_SPEED = -7
ENEMY_SPEED = 3
ENEMY_SPAWN_DELAY = 1200
EXPLOSION_ANIMATION_SPEED = 5

# Инициализация экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("StarLancer")

# Загрузка ресурсов
def load_image(path, scale=None, color_key=None):
    image = pygame.image.load(path).convert_alpha()
    if scale:
        image = pygame.transform.scale(image, scale)
    if color_key:
        image.set_colorkey(color_key)
    return image

def load_sound(path):
    return pygame.mixer.Sound(path)

background = load_image('sprites/background.jpg')
player_image = load_image('sprites/player.png', (50, 50))
enemy_image = load_image('sprites/enemy.png', (30, 30))
shot_image = load_image('sprites/shot.png')
explosion_frames = [load_image(f'sprites/explosion/exp_{i}.png', (80, 80), (255, 255, 255)) for i in range(1, 17)]

shoot_sound = load_sound('audio/shoot.wav')
explosion_sound = load_sound('audio/explosion.wav')

# Классы спрайтов
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        self.speed = PLAYER_SPEED

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def shoot(self):
        shoot_sound.play()
        return Bullet(self.rect.centerx, self.rect.top)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = shot_image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = BULLET_SPEED

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect(topleft=(random.randint(0, SCREEN_WIDTH - 30), 0))
        self.speed = ENEMY_SPEED

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.frames = explosion_frames
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=(x, y))
        self.animation_speed = EXPLOSION_ANIMATION_SPEED
        self.frame_counter = 0

    def update(self):
        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.frame_counter = 0
            self.frame_index += 1
            if self.frame_index >= len(self.frames):
                self.kill()
            else:
                self.image = self.frames[self.frame_index]

class UI:
    def __init__(self):
        self.font = pygame.font.SysFont("Timesnewroman", 24)

    def draw_score(self, screen, score):
        score_text = self.font.render(f"Счёт: {score}", True, (255, 255, 255))
        screen.blit(score_text, (12, 12))

# Группы спрайтов
all_sprites, bullets, enemies, explosions = (pygame.sprite.Group(), pygame.sprite.Group(),
                                             pygame.sprite.Group(), pygame.sprite.Group())

# Создание игрока и UI
player: Player = Player()
all_sprites.add(player) #type: ignore
ui = UI()

# Переменные игры
score = 0
running = True
last_enemy_spawn = pygame.time.get_ticks()

pygame.mixer.music.load('audio/background_music.mp3')
pygame.mixer.music.play(-1)

# Частота кадров
clock = pygame.time.Clock()

# Основной игровой цикл
while running:
    clock.tick(FPS)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bullet = player.shoot()
                all_sprites.add(bullet) #type: ignore
                bullets.add(bullet) #type: ignore

    # Появление врагов
    now = pygame.time.get_ticks()
    if now - last_enemy_spawn > ENEMY_SPAWN_DELAY:
        enemy = Enemy()
        all_sprites.add(enemy) #type: ignore
        enemies.add(enemy) #type: ignore
        last_enemy_spawn = now

    all_sprites.update()

    # Проверка столкновений пуль с врагами
    hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for hit in hits:
        explosion_sound.play()
        score += 1
        explosion = Explosion(hit.rect.centerx, hit.rect.centery)
        all_sprites.add(explosion) #type: ignore
        explosions.add(explosion) #type: ignore

    # Проверка столкновений игрока с врагами
    if pygame.sprite.spritecollide(player, enemies, False): #type: ignore
        running = False

    # Отрисовка
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    ui.draw_score(screen, score)

    pygame.display.flip()

# Завершение игры
pygame.mixer.music.stop()
pygame.quit()

