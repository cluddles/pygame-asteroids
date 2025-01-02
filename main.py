#!/usr/bin/env python3

import pygame

from constants import *
from circleshape import CircleShape
from game import Game

def keep_running():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        return False
    return True

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game = Game()
    clock = pygame.time.Clock()
    dt = 0
    while (keep_running()):
        game.update(dt)
        game.render(screen)
        dt = clock.tick(FPS) / 1000

if __name__ == "__main__":
    main()
