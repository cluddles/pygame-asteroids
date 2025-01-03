#!/usr/bin/env python3

import pygame

from constants import *
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
    font = pygame.font.Font(None, 32) # freesansbold built-in
    game_over_text = font.render("Game Over. R to Restart", True, (255, 255, 255, 255))
    pygame.display.set_caption("Asteroids")
    game = Game()
    clock = pygame.time.Clock()
    dt = 0
    while (keep_running()):
        # logic tick
        game.update(dt)
        # render
        screen.fill((0,0,0))
        game.render(screen)
        # game over
        if game.game_over:
            screen.blit(game_over_text, (200, 200))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                game = Game()
        pygame.display.flip()
        dt = clock.tick(FPS) / 1000

if __name__ == "__main__":
    main()
