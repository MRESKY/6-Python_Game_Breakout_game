import pygame

class UIManager:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('Segoe UI Emoji', 36)
        self.small_font = pygame.font.SysFont('None', 24)
        self.big_font = pygame.font.SysFont('None', 100)

    def draw_hud(self, screen, score, lives, level):
        """Draws the heads-up display (HUD) showing score and lives."""
        score_text = self.font.render(f'Score: {score}', True, (255, 255, 255))
        lives_text = self.font.render('❤️ ' * lives, True, (255, 255, 255))
        level_text = self.font.render(f'Level: {level}', True, (255, 255, 255))

        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (300, 10))
        screen.blit(level_text, (650, 10))

    def draw_game_over(self, screen, score):
        """Draws the game over screen with the final score."""
        game_over_text = self.font.render('Game Over', True, (255, 0, 0))
        score_text = self.small_font.render(f'Final Score: {score}', True, (255, 255, 255))
        
        # Get screen dimensions
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        
        # Center the text
        game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2 - 50))
        score_rect = score_text.get_rect(center=(screen_width // 2, screen_height // 2 - 10))
        
        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)

    def get_level_and_count_down(self, screen, level):
        """Draws a countdown timer on the screen."""
        screen_width = screen.get_width()
        screen_height = screen.get_height()

        get_level_text = self.big_font.render(f'Get Ready for Level {level}!', True, (255, 255, 255))
        text_rect = get_level_text.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
        screen.blit(get_level_text, text_rect)
        pygame.display.flip()
        pygame.time.delay(1000)
        
        for count in range(3, 0, -1):
            screen.fill((0, 0, 0))  # Clear screen
            countdown_text = self.big_font.render(str(count), True, (255, 255, 255))
            text_rect = countdown_text.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(countdown_text, text_rect)
            pygame.display.flip()
            pygame.time.delay(1000)  # Wait for 1 second