from entities.game_object import GameObject
import pygame

class Ball(GameObject):
    """
    Docstring for Ball
    """
    def __init__(self, x, y):
        super().__init__(x, y, width=20, height=20)
        self.color = (255, 255, 255)  # White color
        self.radius = self.width / 2
        self.velocity = pygame.Vector2(4, -4)  # Initial velocity

    def move(self):
        self.x += self.velocity.x
        self.y += self.velocity.y
        self.rect.x = self.x
        self.rect.y = self.y

    def bounce_x(self):
        self.velocity.x = -self.velocity.x
    
    def bounce_y(self):
        self.velocity.y = -self.velocity.y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x) + self.radius, int(self.y) + self.radius), self.radius)
    
    def update(self):
        self.move()

        if self.x <= 0 or self.x + self.width >= 800:  # Assuming screen width is 800
            self.bounce_x()
        if self.y <= 0:  # Top of the screen
            self.bounce_y()

    def get_rect(self):
        return self.rect
