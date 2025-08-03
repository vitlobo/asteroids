import pygame
from vectorsprites import Point
from constants import SHOT_RADIUS


class Shot(Point):
    def __init__(self, position, heading, shooter, ttl, velocity):
        super().__init__(position, heading, SHOT_RADIUS)
        self.shooter = shooter
        self.ttl = ttl
        self.velocity = velocity
        self.bounding_rect = pygame.Rect(1, 1, 1, 1)
        
    def draw(self, screen):
        self.bounding_rect = pygame.draw.circle(screen, "white", (self.position), self.radius, width = 2)
        #pygame.draw.rect(screen, "white", self.bounding_rect, 1)

    def update(self, dt):
        self.ttl -= 1
        if self.ttl <= 0:
            self.kill()
        Point.move(self, dt)

    def check_bullet_collision(self, other):
        if self.ttl > 0 and self.check_collisions(other):
            self.ttl = 0
            return True
        else:
            return False