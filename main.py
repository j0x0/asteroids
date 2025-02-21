import sys
import pygame
from player import *
from constants import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    time = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player( (SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for astroid in asteroids:
            if astroid.isCollision(player):
                print("Game over!")
                sys.exit()
        
        screen.fill("black")
        
        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()
        dt = (time.tick(60))/1000


if __name__ == "__main__":
    main()