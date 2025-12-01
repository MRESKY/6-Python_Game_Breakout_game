
class ScoreManager:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.lives = 3
        self.high_score = self.load_high_score()
    
    def add_score(self, points):
        self.score += points
        if self.score > self.high_score:
            self.high_score = self.score

    def lose_life(self):
        self.lives -= 1

    def is_game_over(self):
        return self.lives <= 0
    
    def load_high_score(self, filename=".\data\highscore\highscore.txt"):
        try:
            with open(filename, "r") as file:
                return int(file.read().strip())
        except (FileNotFoundError, ValueError):
            return 0
        
    def save_high_score(self, filename=".\data\highscore\highscore.txt"):
        with open(filename, "w") as file:
            file.write(str(self.high_score))
