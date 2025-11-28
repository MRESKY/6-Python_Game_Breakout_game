import pygame
from entities.paddle import Paddle
from entities.ball import Ball
from systems.collision import CollisionSystem
from systems.ui import UIManager
from entities.brick import Brick
from systems.level import LevelManager
from systems.score import ScoreManager


class Breakoutgame:
    def __init__(self, paddle: Paddle = None, ball: Ball = None, collision_system: CollisionSystem = None):
        # Initialize pygame
        pygame.init()

        #Screen setup
        self.screen_width = 800
        self.screen_height = 600
        pygame.display.set_caption("Breakout Game")
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = True

        self.paddle = paddle or Paddle(self.screen_width / 2 - 50, self.screen_height - 50)
        self.ball = ball or Ball(self.screen_width / 2 - 10, self.screen_height / 2 - 10, radius=8)
        self.collision_system = collision_system or CollisionSystem()

        self.ui_manager = UIManager()
        self.score = 0
        self.lives = 3
        self.level = 1

    def handle_inputs(self):
        # poll for events
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

    def update(self):
        # Update game objects
        self.paddle.update()
        self.ball.update()
        self.collision_system.check_ball_paddle(self.ball, self.paddle)
        

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear screen with black
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        self.ui_manager.draw_hud(self.screen, self.score, self.lives, self.level)
        pygame.display.flip()  # Update the full display Surface to the screen
        

    def run(self):
        while self.running:
            # limits FPS to 60
            self.clock.tick(self.fps)

            # Handle user inputs
            self.handle_inputs()
            self.update()
            self.draw()
            

        pygame.quit()

if __name__ == "__main__":
    game = Breakoutgame()
    game.run()

