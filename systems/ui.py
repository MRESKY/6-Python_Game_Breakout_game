import pygame

class UIManager:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('Segoe UI Emoji', 36)
        self.small_font = pygame.font.SysFont('None', 24)

    def draw_hud(self, screen, score, lives, level):
        """Draws the heads-up display (HUD) showing score and lives."""
        score_text = self.font.render(f'Score: {score}', True, (255, 255, 255))
        lives_text = self.font.render('❤️ ' * lives, True, (255, 255, 255))
        level_text = self.font.render(f'Level: {level}', True, (255, 255, 255))

        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (300, 10))
        screen.blit(level_text, (650, 10))