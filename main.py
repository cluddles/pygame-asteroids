#!/usr/bin/env python3

import pygame

from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_loop(screen)

def wrap(thing, screen):
    if not isinstance(thing, CircleShape):
        return
    w = screen.get_width()
    h = screen.get_height()
    r = thing.radius
    if thing.position.x + r < 0:
        thing.position.x += w + r * 2
    elif thing.position.x - r >= w:
        thing.position.x -= w + r * 2
    if thing.position.y + r < 0:
        thing.position.y += h + r * 2
    elif thing.position.y - r >= h:
        thing.position.y -= h + r * 2

def game_loop(screen):
    clock = pygame.time.Clock()
    dt = 0
    running = True
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    Shot.containers = (updatable, drawable, shots)
    while running:
        # nice if we can quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        # logic
        for thing in updatable:
            thing.update(dt)
            wrap(thing, screen)
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game over!")
                running = False
            for shot in shots:
                if asteroid.is_colliding(shot):
                    asteroid.split()
                    shot.kill()
        # render
        screen.fill((0,0,0))
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(FPS) / 1000

if __name__ == "__main__":
    main()
