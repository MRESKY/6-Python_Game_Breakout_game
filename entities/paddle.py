from entities.game_object import GameObject
import pygame

class Paddle(GameObject):
    """
    Paddle class representing a player's paddle in the game.
    """
    def __init__(self, x, y):
        super().__init__(x, y, width=100, height=20)
        self.color = (255, 255, 255)  # White color
        self.speed = 5
        
    def move_left(self):
        self.x -= self.speed
        self.x = max(0, self.x)
        self.rect.x = self.x

    def move_right(self, screen_width):
        self.x += self.speed
        self.x = min(screen_width - self.width, self.x)
        self.rect.x = self.x

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right(800)  # Assuming screen width is 800

    def get_rect(self):
        return self.rect