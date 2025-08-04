import pygame
import random
from asteroid import Asteroid
from constants import *


class AsteroidField(pygame.sprite.Sprite):
    
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-60, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + 60, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -60),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + 60
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, position, velocity, asteroid_type):
        asteroid = Asteroid(position, asteroid_type)
        asteroid.velocity = velocity   

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            asteroid_type = random.randint(0, 2) 
            position = edge[1](random.uniform(0, 1))
            self.spawn(position, velocity, asteroid_type)