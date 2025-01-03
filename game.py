#!/usr/bin/env python3

import pygame

from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

class Game:
    def __init__(self):
        self.game_over = False
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()

        # This is a bit questionable; the groups are object vars but the container specs are class vars
        Player.containers = (self.updatable, self.drawable)
        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)
        AsteroidField.containers = (self.updatable)
        Shot.containers = (self.updatable, self.drawable, self.shots)

        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.asteroid_field = AsteroidField()

    def wrap(self, thing):
        if not isinstance(thing, CircleShape):
            return
        w = SCREEN_WIDTH
        h = SCREEN_HEIGHT
        r = thing.radius
        if thing.position.x + r < 0:
            thing.position.x += w + r * 2
        elif thing.position.x - r >= w:
            thing.position.x -= w + r * 2
        if thing.position.y + r < 0:
            thing.position.y += h + r * 2
        elif thing.position.y - r >= h:
            thing.position.y -= h + r * 2

    def update(self, dt):
        for thing in self.updatable:
            thing.update(dt)
            self.wrap(thing)
        for asteroid in self.asteroids:
            if not self.game_over and asteroid.is_colliding(self.player):
                print("Game over!")
                self.game_over = True
                self.player.kill()
            for shot in self.shots:
                if asteroid.is_colliding(shot):
                    asteroid.split()
                    shot.kill()

    def render(self, screen):
        for thing in self.drawable:
            thing.draw(screen)
