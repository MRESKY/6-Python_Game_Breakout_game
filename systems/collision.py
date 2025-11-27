from abc import ABC, abstractmethod


class iCollisionSystem(ABC):
    """
    Base class for collision detection systems.
    """
    @staticmethod
    @abstractmethod
    def check_ball_paddle(ball, paddle):
        """Override in child class to check collision between two objects."""
        pass

    @staticmethod
    @abstractmethod
    def check_ball_brick(ball, brick):
        """Override in child class to check collision between two objects."""
        pass

    @staticmethod
    @abstractmethod
    def check_ball_walls(ball, wall):
        """Override in child class to check collision between two objects."""
        pass


class CollisionSystem(iCollisionSystem):
    @staticmethod
    def check_ball_paddle(ball, paddle):
        if ball.get_rect().colliderect(paddle.get_rect()):
            ball.bounce_y()

            hit_pos = ball.x - paddle.x
            paddle_center = paddle.width / 2
            offset = (hit_pos - paddle_center) / paddle_center
            ball.velocity.x += offset
            return True
        return False

    @staticmethod
    def check_ball_brick(ball, brick):
        # Implement collision detection logic between ball and brick
        pass

    @staticmethod
    def check_ball_walls(ball, wall):
        # Implement collision detection logic between ball and walls
        pass