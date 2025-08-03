import pygame
from constants import *
from vectorsprites import *
from shooter import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


class Python_Asteroids():
    def __init__(self):
        self.paused = False
        self.game_mode = "not_playing"
        self.player = None
        self.lives = 0
        self.score = 0

    def start_new_game(self):
        self.game_mode = "playing"
        self.starting_lives = 3
        self.create_lives_list()
        self.create_new_plaer()
        self.score = 0
        self.run_length = 1

    def create_lives_list(self):
        self.lives_list = []

    def play_game(self):

        print("Starting Asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.mouse.set_visible(False)
        pygame.display.set_caption("Python Asteroids")
        clock = pygame.time.Clock()
        fps = 0.0
        dt = 0

        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()
        jet_thrust = pygame.sprite.Group()

        Player.containers = (updatable, drawable)
        Jet_Thrust.containers = (jet_thrust, updatable, drawable)
        Asteroid.containers = (asteroids, updatable, drawable)
        AsteroidField.containers = (updatable)
        Shot.containers = (shots, updatable, drawable)

        player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
        asteroid_field = AsteroidField()

        #game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            screen.fill("black")
            updatable.update(dt)
            for a in asteroids:
                if a.check_collisions(player) == True:
                    print("Game over!")
                    exit()
            for a in asteroids:
                for s in shots:
                    if s.check_bullet_collision(a):
                        s.kill()
                        self.score += a.split()
            for d in drawable:
                keep_in_frame(d, SCREEN_WIDTH, SCREEN_HEIGHT)
                d.draw(screen)
            #fps
            dt = (clock.tick(60) / 1000)
            fps = round(clock.get_fps(), 2)
            show_fps(screen, fps)
            show_score(screen, self.score)

            pygame.display.flip()

def keep_in_frame(sprite, width, height):
        if sprite.position.x < 0:
            sprite.position.x = width
            
        if sprite.position.x > width:
            sprite.position.x = 0
        
        if sprite.position.y < 0:
            sprite.position.y = height
            
        if sprite.position.y > height:
            sprite.position.y = 0

def show_score(screen, score):
    font = pygame.font.SysFont("arial", 15)
    score_string = str(score)
    score_text = font.render(f"SCORE: {score_string}", True, (255, 255, 255))
    score_rect = score_text.get_rect(centerx=35, centery=10)
    screen.blit(score_text, score_rect)

def show_fps(screen, fps):
    font = pygame.font.SysFont("arial", 15)
    fps_string = str(fps)
    fps_text = font.render(f"FPS: {fps_string}", True, (255, 255, 255))
    fps_rect = fps_text.get_rect(centerx=(SCREEN_WIDTH - 35), centery=10)
    screen.blit(fps_text, fps_rect)

def fill(self, color):
    pygame.Surface.fill(color)

game = Python_Asteroids()
game.play_game()