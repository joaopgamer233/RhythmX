# Configuration for RhythmX Arrow Game

import pygame

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Arrow settings
ARROW_SPEED = 5
ARROW_SIZE = 75
HIT_ZONE_Y = 100  # Y position of the hit zone

# Key mappings
KEYS = {
    'left': pygame.K_LEFT,
    'down': pygame.K_DOWN,
    'up': pygame.K_UP,
    'right': pygame.K_RIGHT
}

# Directions
DIRECTIONS = ['left', 'down', 'up', 'right']

# Scoring
PERFECT_SCORE = 100
GOOD_SCORE = 50
MISS_SCORE = 0

# Timing windows (in frames)
PERFECT_WINDOW = 5
GOOD_WINDOW = 15
