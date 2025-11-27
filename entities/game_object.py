from abc import ABC, abstractmethod
import pygame

class GameObject(ABC):
    """Base class for all game objects."""
    def __init__(self, x,y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
    
    @abstractmethod
    def draw(self, screen):
        """Ovverride di child class to draw the game object."""
        pass

    @abstractmethod
    def update(self):
        """Ovverride di child class to update the game object."""
        pass

    @abstractmethod
    def get_rect(self, event):
        """Ovverride di child class to rect object."""
        pass
