import pygame
from entities.paddle import Paddle
from entities.ball import Ball
from systems.collision import CollisionSystem
from systems.ui import UIManager
from entities.brick import Brick
from systems.level import LevelManager
from systems.score import ScoreManager


class Breakoutgame:
    def __init__(self, paddle: Paddle = None, ball: Ball = None, 
                 collision_system: CollisionSystem = None, score_manager: ScoreManager = None,
                 level_manager: LevelManager = None):
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


        self.collision_system = collision_system or CollisionSystem()
        self.score_manager = score_manager or ScoreManager()
        self.level_manager = level_manager or LevelManager()
    

        self.ui_manager = UIManager()
        self.bricks = []
        self.active_bricks = [None]
        self.reset_game()

    def reset_game(self):
        self.paddle = Paddle(self.screen_width / 2 - 50, self.screen_height - 50)
        self.ball = Ball(self.paddle.x + self.paddle.width // 2, self.paddle.y - self.paddle.height)
        self.bricks = self.level_manager.load_level(self.score_manager.level)


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

        destroyed = self.collision_system.check_ball_brick(self.ball, self.bricks)
        for brick in destroyed:
            self.score_manager.add_score(brick.point_value)

        self.score_manager.score
        self.score_manager.lives
        self.score_manager.level


        self.active_bricks = [b for b in self.bricks if not b.is_destroyed]
        if len(self.active_bricks) == 0:
            self.score_manager.level +=1
            self.bricks = self.level_manager.next_level()
            self.ui_manager.get_level_and_count_down(self.screen, self.score_manager.level)
            self.paddle = Paddle(self.screen_width / 2 - 50, self.screen_height - 50)
            self.ball = Ball(self.paddle.x + self.paddle.width // 2, self.paddle.y - self.paddle.height)

        if self.ball.y > self.screen_height:
            self.score_manager.lose_life()
            if self.score_manager.lives <= 0:
                self.ui_manager.draw_game_over(self.screen, self.score_manager.score)
                self.running = False
            else:
                self.ui_manager.get_level_and_count_down(self.screen, self.score_manager.level)
                self.paddle = Paddle(self.screen_width / 2 - 50, self.screen_height - 50)
                self.ball = Ball(self.paddle.x + self.paddle.width // 2, self.paddle.y - self.paddle.height)


        

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear screen with black
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        self.ui_manager.draw_hud(self.screen, self.score_manager.score, self.score_manager.lives, self.score_manager.level)
        for brick in self.bricks:
            brick.draw(self.screen)
        
        
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

