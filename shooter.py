from vectorsprites import *
from shot import *

class Shooter(VectorSprite):
    def __init__(self, position, heading, point_list):
        super().__init__(position, heading, point_list)
        self.shoot_cooldown = 0

    def shoot(self, heading, ttl, velocity):
        position = pygame.Vector2(self.position[0], self.position[1])
        shot = Shot(position, heading, self, ttl, velocity)