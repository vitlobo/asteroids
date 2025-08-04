import pygame, random
from vectorsprites import *


class Asteroid(VectorSprite):

    large_asteroid = 0
    medium_asteroid = 1
    small_asteroid = 2

    asteroid_scales = (2.5, 1.5, 0.6)
    asteroid_velocities = (1.5, 4.0, 6.0)

    asteroid_shape = 1

    def __init__(self, position, asteroid_type):

        scale = Asteroid.asteroid_scales[asteroid_type]
        velocity = Asteroid.asteroid_velocities[asteroid_type]
        self.asteroid_type = asteroid_type
        heading = random.uniform(-velocity, velocity), random.uniform(-velocity, velocity)
        self.rotation = 0
        point_list = self.create_point_list()
        new_point_list = [self.scale(point, scale) for point in point_list]
        self.bounding_rect = pygame.Rect(1, 1, 1, 1)
        super().__init__(position, heading, new_point_list)
    
    def create_point_list(self):
        if ( Asteroid.asteroid_shape == 1):
            point_list = [(-4,-12), (6,-12), (13, -4), (13, 5), (6, 13), (0,13), (0,4),\
                     (-8,13), (-15, 4), (-7,1), (-15,-3)]
 
        elif (Asteroid.asteroid_shape == 2):
            point_list = [(-6,-12), (1,-5), (8, -12), (15, -5), (12,0), (15,6), (5,13),\
                         (-7,13), (-14,7), (-14,-5)]
            
        elif (Asteroid.asteroid_shape == 3):
            point_list = [(-7,-12), (1,-9), (8,-12), (15,-5), (8,-3), (15,4), (8,12),\
                         (-3,10), (-6,12), (-14,7), (-10,0), (-14,-5)]            

        elif (Asteroid.asteroid_shape == 4):
            point_list = [(-7,-11), (3,-11), (13,-5), (13,-2), (2,2), (13,8), (6,14),\
                         (2,10), (-7,14), (-15,5), (-15,-5), (-5,-5), (-7,-11)]

        Asteroid.asteroid_shape += 1

        if Asteroid.asteroid_shape == 5:
            Asteroid.asteroid_shape = 1
        return point_list


    def draw(self, screen):
        self.bounding_rect = pygame.draw.aalines(screen, "white", True, VectorSprite.get_point_list(self))
        #pygame.draw.rect(screen, "white", self.bounding_rect, 1)

    def update(self, dt):
        self.position += (self.velocity * dt)
        self.rotation += 1

    def split(self):
        self.kill()
        add_to_score = 0
        if self.asteroid_type == Asteroid.small_asteroid:
            add_to_score = 200
            return add_to_score
        elif self.asteroid_type == Asteroid.medium_asteroid:
            new_asteroid_type = 2
            multiplier = 2.0
            add_to_score = 100
        else: 
            new_asteroid_type = 1
            multiplier = 1.5
            add_to_score = 50

        random_angle = random.uniform(20, 70)
        random_pos_1 = random.uniform(5, 15)

        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(0 - random_angle)
        position_1 = pygame.Vector2(self.position[0] - random_pos_1, self.position[1] - random_pos_1)
        position_2 = pygame.Vector2(self.position[0] + random_pos_1, self.position[1] + random_pos_1)

        new_asteroid_1 = Asteroid(position_1, new_asteroid_type)
        new_asteroid_2 = Asteroid(position_2, new_asteroid_type)
        new_asteroid_1.velocity = new_velocity_1 * multiplier
        new_asteroid_2.velocity = new_velocity_2 * multiplier
        return add_to_score