import pygame
import random
import os
from config import *

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RhythmX")
clock = pygame.time.Clock()

# Load assets
def load_image(name, folder='arrows'):
    path = os.path.join('assets', 'images', folder, name)
    if os.path.exists(path):
        image = pygame.image.load(path)
        return pygame.transform.scale(image, (ARROW_SIZE, ARROW_SIZE))
    else:
        # Placeholder: create a colored surface
        surf = pygame.Surface((ARROW_SIZE, ARROW_SIZE))
        if 'left' in name:
            surf.fill(RED)
        elif 'down' in name:
            surf.fill(GREEN)
        elif 'up' in name:
            surf.fill(BLUE)
        elif 'right' in name:
            surf.fill(YELLOW)
        else:
            surf.fill(WHITE)
        return surf

arrow_images = {
    'left': load_image('left.png'),
    'down': load_image('down.png'),
    'up': load_image('up.png'),
    'right': load_image('right.png')
}

class Arrow:
    def __init__(self, direction):
        self.direction = direction
        self.image = arrow_images[direction]
        self.x = SCREEN_WIDTH // 2 - ARROW_SIZE // 2
        self.y = SCREEN_HEIGHT
        self.hit = False

    def update(self):
        self.y -= ARROW_SPEED

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def is_off_screen(self):
        return self.y < -ARROW_SIZE

    def check_hit(self, key_pressed):
        if self.direction == key_pressed and HIT_ZONE_Y - PERFECT_WINDOW <= self.y <= HIT_ZONE_Y + PERFECT_WINDOW:
            return 'perfect'
        elif self.direction == key_pressed and HIT_ZONE_Y - GOOD_WINDOW <= self.y <= HIT_ZONE_Y + GOOD_WINDOW:
            return 'good'
        return None

class Game:
    def __init__(self):
        self.arrows = []
        self.score = 0
        self.spawn_timer = 0
        self.spawn_interval = 60  # frames

    def update(self):
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_timer = 0
            direction = random.choice(DIRECTIONS)
            self.arrows.append(Arrow(direction))

        for arrow in self.arrows[:]:
            arrow.update()
            if arrow.is_off_screen():
                self.arrows.remove(arrow)
                self.score += MISS_SCORE

    def draw(self, screen):
        screen.fill(BLACK)
        # Draw hit zone
        pygame.draw.rect(screen, WHITE, (0, HIT_ZONE_Y - 5, SCREEN_WIDTH, 10))
        for arrow in self.arrows:
            arrow.draw(screen)
        # Draw score
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))

    def handle_input(self, key):
        for arrow in self.arrows[:]:
            result = arrow.check_hit(key)
            if result:
                self.arrows.remove(arrow)
                if result == 'perfect':
                    self.score += PERFECT_SCORE
                elif result == 'good':
                    self.score += GOOD_SCORE
                break

def main():
    game = Game()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == KEYS['left']:
                    game.handle_input('left')
                elif event.key == KEYS['down']:
                    game.handle_input('down')
                elif event.key == KEYS['up']:
                    game.handle_input('up')
                elif event.key == KEYS['right']:
                    game.handle_input('right')

        game.update()
        game.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
