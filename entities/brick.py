from entities.game_object import GameObject
import pygame


class Brick(GameObject):
    def __init__(self, x, y, color=(255, 100, 100)):
        super().__init__(x, y, width=75, height=20)
        self.color = color
        self.health = 1
        self.is_destroyed = False
        self.point_value = 10

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            self.is_destroyed = True
            return True
        return False
    
    def draw(self, screen):
        if not self.is_destroyed:
            pygame.draw.rect(screen, self.color, self.get_rect())
            pygame.draw.rect(screen, (0, 0, 0), self.get_rect(), 2)  # Border

    def update(self):
        pass  # Bricks are static; no update logic needed

    def get_rect(self):
        return self.rect