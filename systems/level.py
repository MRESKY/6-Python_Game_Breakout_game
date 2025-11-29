from entities.brick import Brick

class LevelManager:
    def __init__(self):
        self.level = 1
        self.bricks_layout = self.create_level_layout()

    def create_level_layout(self):
        """
        Pattern layout
        """
        return {
            1: [
                [0, 0, 0, 0, 0, 0, 1, 0],    
            ],

            2: [
                [1, 1, 1, 1, 1, 1, 1, 1],  # Row 1
                [1, 1, 1, 1, 1, 1, 1, 1],  # Row 2
                [1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0]  # Row 3
            ],
            3: [
                [2, 2, 2, 2, 2, 2, 2, 2],
                [1, 1, 1, 1, 1, 1, 1, 1],
                [2, 2, 2, 2, 2, 2, 2, 2],
                [1, 1, 1, 1, 1, 1, 1, 1],
            ],
            # More levels...
        }
    
    def load_level(self, level_number):
        bricks = []
        layout = self.bricks_layout.get(level_number,self.bricks_layout[1])

        brick_width = 75
        brick_height = 20
        padding = 5
        offset_x = 50
        offset_y = 100

        colors = {
            1: (255, 100, 100),
            2: (100, 100, 255),
            3: (100, 255, 100),
        }

        for row_index, row in enumerate(layout):
            for column_index, brick_type in enumerate(row):
                if brick_type == 0:
                    continue

                x = offset_x + column_index * (brick_width + padding)
                y = offset_y + row_index * (brick_height + padding)

                brick = Brick(x, y)
                brick.color = colors[brick_type]
                brick.health = brick_type

                bricks.append(brick)
        
        return bricks
    
    def next_level(self):
        self.level += 1
        return self.load_level(self.level)



