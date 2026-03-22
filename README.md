# RhythmX Arrow Rhythm Game

A simple arrow-based rhythm game built with Pygame.

## How to Play

- Arrows will spawn from the bottom and move upwards.
- Press the corresponding arrow key (Left, Down, Up, Right) when the arrow reaches the white hit zone at the top.
- Score points based on timing: Perfect (100 points) or Good (50 points).
- Misses give 0 points.

## Installation

1. Install Python 3.x
2. Install dependencies: `pip install -r requirements.txt`
3. Run the game: `python main.py`

## Assets

Place arrow images in `assets/images/arrows/`:
- left_arrow.png
- down_arrow.png
- up_arrow.png
- right_arrow.png

If images are not found, the game uses colored rectangles as placeholders.

## Configuration

Edit `config.py` to change game settings like speed, scoring, etc.

## Troubleshooting

- If the game doesn't start, ensure Pygame is installed.
- On some systems, you may need to install additional dependencies for Pygame (e.g., SDL).