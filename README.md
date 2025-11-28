# 🎮 Breakout Game

A classic **Breakout** arcade game built with Python and Pygame. This project demonstrates object-oriented programming principles, game development patterns, and clean code architecture.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Pygame](https://img.shields.io/badge/pygame-v2.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🎯 Features

- **Classic Breakout Gameplay**: Break all the bricks with a bouncing ball
- **Multiple Levels**: Progressive difficulty with different brick patterns
- **Score System**: Points for breaking bricks with high score tracking
- **Lives System**: Start with 3 lives, lose one when ball goes off screen
- **Smooth Controls**: Responsive paddle movement with keyboard controls
- **Visual Effects**: Colorful bricks, smooth ball movement, and clean UI
- **Game Over Screen**: Final score display and game over detection
- **Level Progression**: Countdown timer between levels

## 🎮 Controls

- **Left Arrow Key** (`←`): Move paddle left
- **Right Arrow Key** (`→`): Move paddle right
- **ESC**: Quit game

## 📋 Requirements

- Python 3.7 or higher
- Pygame 2.0 or higher

## 🚀 Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MRESKY/6-Python_Game_Breakout_game.git
   cd 6-Python_Game_Breakout_game
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game:**
   ```bash
   python main.py
   ```

## 🏗️ Project Structure

```
6-Python_Game_Breakout_gane/
│
├── main.py                 # Entry point
├── README.md              # Project documentation
├── requirements.txt       # Dependencies
├── LICENSE               # MIT License
└── setup.py              # Package setup
│
├── entities/             # Game entities
│   ├── __init__.py
│   ├── game_object.py    # Base class for all game objects
│   ├── ball.py           # Ball entity
│   ├── paddle.py         # Paddle entity
│   └── brick.py          # Brick entity
│
├── game/                 # Main game logic
│   ├── __init__.py
│   └── game.py           # Main game class
│
└── systems/              # Game systems
    ├── collision.py      # Collision detection
    ├── level.py          # Level management
    ├── score.py          # Score and lives management
    └── ui.py             # User interface
```

## 🎯 Game Mechanics

### Scoring

- **Basic Brick**: 10 points
- **Special Bricks**: Variable points based on type
- **High Score**: Automatically saved and loaded

### Lives

- Start with 3 lives
- Lose a life when ball goes off the bottom of the screen
- Game over when all lives are lost

### Levels

- Multiple levels with different brick patterns
- Increasing difficulty as you progress
- Countdown timer between levels

## 🛠️ Architecture

This project follows clean code principles and design patterns:

- **Entity-Component System**: Modular game objects
- **Abstract Base Classes**: Consistent interface for game objects
- **Dependency Injection**: Flexible system initialization
- **Single Responsibility**: Each class has a specific purpose
- **Collision System**: Dedicated collision detection logic
- **UI Management**: Separate UI rendering system

### Key Classes

- `GameObject`: Abstract base class for all game entities
- `Ball`: Handles ball movement and physics
- `Paddle`: Player-controlled paddle
- `Brick`: Destructible game objects
- `CollisionSystem`: Handles collision detection
- `ScoreManager`: Manages score and lives
- `LevelManager`: Handles level progression
- `UIManager`: Renders game interface

## 🎨 Customization

### Adding New Levels

Edit `systems/level.py` and add new patterns to the `bricks_layout` dictionary:

```python
3: [
    [3, 3, 3, 3, 3, 3, 3, 3],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2, 2],
],
```

### Changing Colors

Modify the `colors` dictionary in `systems/level.py`:

```python
colors = {
    1: (255, 100, 100),  # Red
    2: (100, 100, 255),  # Blue
    3: (100, 255, 100),  # Green
}
```

### Adjusting Game Physics

Modify ball speed in `entities/ball.py`:

```python
self.velocity = pygame.Vector2(4, -4)  # Increase for faster ball
```

## 🐛 Troubleshooting

### Common Issues

1. **Pygame not found**: Make sure pygame is installed

   ```bash
   pip install pygame
   ```

2. **Python version error**: Ensure Python 3.7+ is installed

   ```bash
   python --version
   ```

3. **Font rendering issues**: The game uses system fonts, ensure your system has the required fonts

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by the classic Atari Breakout game
- Built with [Pygame](https://www.pygame.org/)
- Thanks to the Python community for excellent documentation

## 📧 Contact

**MRESKY** - [GitHub](https://github.com/MRESKY)

Project Link: [https://github.com/MRESKY/6-Python_Game_Breakout_game](https://github.com/MRESKY/6-Python_Game_Breakout_game)

---

⭐ **Star this repository if you found it helpful!**
