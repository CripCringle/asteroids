import pygame
from circleshape import *
from constants import *
from logger import *
import random
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity * dt

    def get_score_value(self):
        """Return points based on asteroid size."""
        if self.radius <= ASTEROID_MIN_RADIUS:
            return SCORE_SMALL_ASTEROID
        elif self.radius <= ASTEROID_MIN_RADIUS * 2:
            return SCORE_MEDIUM_ASTEROID
        else:
            return SCORE_LARGE_ASTEROID

    def split(self):
        score = self.get_score_value()
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return score
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(angle)
        new_velocity2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1 * 1.2
        asteroid2.velocity = new_velocity2 * 1.2
        return score