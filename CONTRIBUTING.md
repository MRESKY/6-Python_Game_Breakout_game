# Breakout Game - Development Guide

## Development Setup

### Prerequisites

- Python 3.7+
- pip (Python package manager)
- Git

### Setting up Development Environment

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MRESKY/6-Python_Game_Breakout_game.git
   cd 6-Python_Game_Breakout_game
   ```

2. **Create virtual environment:**

   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install -e .[dev]  # Install development dependencies
   ```

## Code Style

This project follows PEP 8 Python coding standards. Use the following tools:

- **Black** for code formatting
- **Flake8** for linting
- **MyPy** for type checking

```bash
# Format code
black .

# Lint code
flake8 .

# Type checking
mypy .
```

## Testing

Run tests using pytest:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.
```

## Architecture Overview

### Entity-Component System

The game uses a clean entity-component architecture:

- **Entities**: Game objects like Ball, Paddle, Brick
- **Systems**: Logic handlers like Collision, UI, Level management
- **Components**: Reusable behavior (inherited from GameObject)

### Design Patterns Used

1. **Abstract Factory Pattern**: GameObject base class
2. **Strategy Pattern**: Different collision behaviors
3. **Observer Pattern**: Score and level updates
4. **Singleton Pattern**: Game instance management

## Adding New Features

### Adding a New Entity

1. Create a new file in `entities/`
2. Inherit from `GameObject`
3. Implement required abstract methods:
   - `draw(screen)`
   - `update()`
   - `get_rect()`

Example:

```python
from entities.game_object import GameObject
import pygame

class NewEntity(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, width=50, height=50)
        self.color = (255, 255, 255)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self):
        # Update logic here
        pass

    def get_rect(self):
        return self.rect
```

### Adding a New System

1. Create a new file in `systems/`
2. Implement system logic
3. Add to main game loop in `game/game.py`

### Modifying Game Physics

Game physics constants are located in:

- Ball speed: `entities/ball.py` - `velocity` property
- Paddle speed: `entities/paddle.py` - `speed` property
- Screen dimensions: `game/game.py` - `screen_width`, `screen_height`

## Performance Considerations

1. **Sprite Groups**: Consider using pygame sprite groups for better performance
2. **Collision Optimization**: Current collision uses basic rect collision
3. **Memory Management**: Objects are created/destroyed frequently

## Debugging

### Common Issues

1. **Import Errors**: Check `__init__.py` files exist
2. **Pygame Init**: Ensure pygame.init() is called before creating objects
3. **Path Issues**: Use absolute imports from project root

### Debugging Tools

- Print statements for game state
- Pygame's `pygame.draw.rect()` for visualizing collision boxes
- FPS counter in game loop

## Release Process

1. **Version Bump**: Update version in `setup.py`
2. **Update Changelog**: Document new features/fixes
3. **Run Tests**: Ensure all tests pass
4. **Create Release**: Tag and push to repository

## Contributing Guidelines

1. **Fork** the repository
2. **Create** a feature branch
3. **Write** tests for new features
4. **Follow** code style guidelines
5. **Submit** a pull request

### Commit Message Format

```
type(scope): description

feat(entities): add power-up system
fix(collision): resolve ball stuck in paddle bug
docs(readme): update installation instructions
```

## Future Enhancements

### Planned Features

- [ ] Power-ups (larger paddle, multi-ball, etc.)
- [ ] Sound effects and music
- [ ] Particle effects for brick destruction
- [ ] Save/load game state
- [ ] Online leaderboards
- [ ] Multiple themes/skins

### Technical Improvements

- [ ] Migrate to pygame sprite groups
- [ ] Add unit tests
- [ ] Implement state machine for game states
- [ ] Add configuration system
- [ ] Performance profiling and optimization

## Resources

- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python Style Guide (PEP 8)](https://pep8.org/)
- [Game Programming Patterns](https://gameprogrammingpatterns.com/)
