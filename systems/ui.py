import pygame
from config import (
    BLACK, WHITE, GAME_OVER_COLOR, NEW_RECORD_COLOR, 
    HIGH_SCORE_COLOR, INSTRUCTION_COLOR
)

class UIManager:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('Segoe UI Emoji', 36)
        self.small_font = pygame.font.SysFont('None', 24)
        self.big_font = pygame.font.SysFont('None', 100)

    def draw_hud(self, screen, score, lives, level):
        """Draws the heads-up display (HUD) showing score and lives."""
        score_text = self.font.render(f'Score: {score}', True, WHITE)
        lives_text = self.font.render('❤️ ' * lives, True, WHITE)
        level_text = self.font.render(f'Level: {level}', True, WHITE)

        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (300, 10))
        screen.blit(level_text, (650, 10))

    def draw_game_over(self, screen, score, high_score=None):
        """Draws the game over screen with final score and high score."""
        # Clear screen first
        screen.fill(BLACK)
        
        # Game Over title
        game_over_text = self.big_font.render('GAME OVER', True, GAME_OVER_COLOR)
        
        # Final score
        final_score_text = self.font.render(f'Final Score: {score}', True, WHITE)
        
        # High score
        if high_score is not None:
            if score >= high_score:
                high_score_text = self.font.render('NEW HIGH SCORE!', True, NEW_RECORD_COLOR)
                old_high_text = self.small_font.render(f'Previous: {high_score}', True, INSTRUCTION_COLOR)
            else:
                high_score_text = self.font.render(f'High Score: {high_score}', True, HIGH_SCORE_COLOR)
                old_high_text = None
        else:
            high_score_text = None
            old_high_text = None
        
        # Instructions
        restart_text = self.small_font.render('Press SPACE or ENTER to play again', True, INSTRUCTION_COLOR)
        quit_text = self.small_font.render('Press ESC to quit', True, INSTRUCTION_COLOR)
        
        # Get screen dimensions for centering
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        
        # Position and blit all text
        y_offset = screen_height // 2 - 150
        
        # Game Over title
        title_rect = game_over_text.get_rect(center=(screen_width // 2, y_offset))
        screen.blit(game_over_text, title_rect)
        y_offset += 80
        
        # Final score
        score_rect = final_score_text.get_rect(center=(screen_width // 2, y_offset))
        screen.blit(final_score_text, score_rect)
        y_offset += 50
        
        # High score
        if high_score_text:
            high_score_rect = high_score_text.get_rect(center=(screen_width // 2, y_offset))
            screen.blit(high_score_text, high_score_rect)
            y_offset += 40
            
            if old_high_text:
                old_high_rect = old_high_text.get_rect(center=(screen_width // 2, y_offset))
                screen.blit(old_high_text, old_high_rect)
                y_offset += 40
        
        y_offset += 30
        
        # Instructions
        restart_rect = restart_text.get_rect(center=(screen_width // 2, y_offset))
        screen.blit(restart_text, restart_rect)
        y_offset += 30
        
        quit_rect = quit_text.get_rect(center=(screen_width // 2, y_offset))
        screen.blit(quit_text, quit_rect)

    def get_level_and_count_down(self, screen, level, level_info=None):
        """Draws a countdown timer and level transition with level info."""
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        
        # Clear screen
        screen.fill(BLACK)
        
        # Level info display
        if level_info and level_info.get('name'):
            level_name = level_info['name']
            level_desc = level_info.get('description', '')
            
            # Level name
            level_text = self.big_font.render(f'Level {level}', True, WHITE)
            name_text = self.font.render(level_name, True, NEW_RECORD_COLOR)
            
            # Level description (if available)
            desc_text = None
            if level_desc:
                desc_text = self.small_font.render(level_desc, True, INSTRUCTION_COLOR)
        else:
            # Fallback display
            level_text = self.big_font.render(f'Level {level}', True, WHITE)
            name_text = self.font.render('Get Ready!', True, WHITE)
            desc_text = None
        
        # Position and display level info
        y_offset = screen_height // 2 - 120
        
        level_rect = level_text.get_rect(center=(screen_width // 2, y_offset))
        screen.blit(level_text, level_rect)
        y_offset += 60
        
        name_rect = name_text.get_rect(center=(screen_width // 2, y_offset))
        screen.blit(name_text, name_rect)
        y_offset += 40
        
        if desc_text:
            desc_rect = desc_text.get_rect(center=(screen_width // 2, y_offset))
            screen.blit(desc_text, desc_rect)
        
        pygame.display.flip()
        pygame.time.delay(2000)  # Show level info for 2 seconds
        
        # Countdown
        for count in range(3, 0, -1):
            screen.fill(BLACK)  # Clear screen
            countdown_text = self.big_font.render(str(count), True, WHITE)
            text_rect = countdown_text.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(countdown_text, text_rect)
            pygame.display.flip()
            pygame.time.delay(1000)  # Wait for 1 second

    def draw_pause_screen(self, screen, screen_width, screen_height):
        """Draws the pause screen."""
        pause_text = self.big_font.render('Paused', True, (255, 255, 255))
        screen.blit(pause_text, (screen_width//2 - pause_text.get_width()//2, screen_height//2 - pause_text.get_height()//2))
        pygame.display.flip()
    
    def draw_menu(self, screen, screen_width, screen_height):
        """Draws the main menu screen."""
        title_text = self.big_font.render('BREAKOUT', True, (255, 255, 255))
        start_text = self.small_font.render('Press SPACE to Start', True, (200, 200, 200))

        screen.blit(title_text, (screen_width//2 - title_text.get_width()//2, 200))
        screen.blit(start_text, (screen_width//2 - start_text.get_width()//2, 400))