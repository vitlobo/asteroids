import pygame, math
from math import *
from constants import GAME_SPEED


# Base class for game objects
class VectorSprite(pygame.sprite.Sprite):
    def __init__(self, position, heading, point_list, rotation=0):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = position
        self.heading = heading
        self.rotation = rotation
        self.point_list = point_list
        self.ttl = 30

    def rotate_point(self, point):
        new_point = []
        cos_value = math.cos(radians(self.rotation))
        sin_value = math.sin(radians(self.rotation))
        new_point.append(point[0] * cos_value + point[1] * sin_value)
        new_point.append(point[1] * cos_value - point[0] * sin_value)
        new_point = [int(point) for point in new_point]
        return new_point
    
    def translate_point(self, point):
        new_point =[]
        new_point.append(point[0] + self.position[0])
        new_point.append(point[1] + self.position[1])
        return new_point
    
    def rotate_and_translate(self):
        new_point_list = [self.rotate_point(point) for point in self.point_list]
        self.translated_point_list = [self.translate_point(point) for point in new_point_list]

    def get_point_list(self):
        self.rotate_and_translate()
        return self.translated_point_list
    
    def scale(self, point, scale):
        new_point =[]
        new_point.append(point[0] * scale)
        new_point.append(point[1] * scale)
        new_point = [int(point) for point in new_point]
        return new_point

    def draw(self):
        self.rotate_and_translate()
        return self.translated_point_list

    def move(self, dt):
        self.position[0] += self.heading[0] * dt * GAME_SPEED
        self.position[1] += self.heading[1] * dt * GAME_SPEED

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collisions(self, other):
        if self.bounding_rect.colliderect(other.bounding_rect):
            return True
        else:
            return False
        

class Point(VectorSprite):
    point_list = [(0,0), (1,1), (1,0), (0,1)]
    def __init__(self, position, heading, radius):
        super().__init__(position, heading, self.point_list)
        self.radius = radius
        self.ttl = 35

    def update(self, dt):
        VectorSprite.move(self, dt)