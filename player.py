import pygame
from vectorsprites import *
from shooter import *
from constants import ( PLAYER_TURN_SPEED,
                        PLAYER_BULLET_TTL
                        )
from shot import *


class Player(Shooter):

    acceleration = 9
    deceleration = -0.5
    max_velocity = 450
    bullet_velocity = 10

    def __init__(self, width, height):
        position = pygame.Vector2(width / 2, height / 2)
        heading = pygame.Vector2(0, 0)
        self.jet_thrust = Jet_Thrust(width, height, self)
        point_list = [(0, -10), (6, 10), (3, 7), (-3, 7), (-6, 10)]
        self.rotation = 0
        self.shoot_cooldown = 0
        super().__init__(position, heading, point_list)
    
    def draw(self, screen):
        self.bounding_rect = pygame.draw.aalines(screen, "white", True, VectorSprite.get_point_list(self))
        #pygame.draw.rect(screen, "white", self.bounding_rect, 1)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
        self.jet_thrust.rotation += (PLAYER_TURN_SPEED * dt)
        
    def update(self, dt):
        VectorSprite.move(self, dt)
        self.decrease_thrust(dt)
        keys = pygame.key.get_pressed()
        self.shoot_cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(0 - dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_ESCAPE]:
            exit()
        if keys[pygame.K_w]:
            self.increase_thrust(dt)
            self.jet_thrust.accelerating = True
        else:
            self.jet_thrust.accelerating = False

    def change_velocity(self, dx, dy):
        self.heading[0] += dx
        self.heading[1] += dy
        self.jet_thrust.heading[0] += dx
        self.jet_thrust.heading[1] += dy

    def increase_thrust(self, dt):
        if math.hypot(self.heading[0], self.heading[1]) > self.max_velocity * dt:
            return
        dx = self.acceleration * math.sin(radians(self.rotation)) * -1 * dt
        dy = self.acceleration * math.cos(radians(self.rotation)) * -1 * dt
        self.change_velocity(dx, dy)

    def decrease_thrust(self, dt):
        if (self.heading[0] == 0 and self.heading[1] == 0):
            return
        dx = self.heading[0] * self.deceleration * dt
        dy = self.heading[1] * self.deceleration * dt
        self.change_velocity(dx, dy)

    def shoot(self):
        if self.shoot_cooldown > 0:
            return
        PLAYER_SHOOT_COOLDOWN = 0.3
        vx = self.bullet_velocity * math.sin(radians(self.rotation)) * -1
        vy = self.bullet_velocity * math.cos(radians(self.rotation)) * -1
        heading = pygame.Vector2(vx, vy)
        Shooter.shoot(self, heading, PLAYER_BULLET_TTL, self.bullet_velocity)
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

class Jet_Thrust(VectorSprite):
    point_list = [(-3, 7), (0, 13), (3, 7)]

    def __init__(self, width, height, player):
        position = pygame.Vector2(width // 2, height // 2)
        heading = pygame.Vector2(0, 0)
        self.accelerating = False
        self.player = player
        super().__init__(position, heading, self.point_list)

    def draw(self, screen):
        if self.accelerating == True:
            self.color = ("white")
        else:
            self.color = ("black")
        pygame.draw.aalines(screen, self.color, True, VectorSprite.get_point_list(self))
    
    def update(self, dt):
        VectorSprite.move(self, dt)