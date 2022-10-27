import sys
import pygame
from game_character import BlueBomber


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((200, 200))
        self.screen.fill((122, 156, 245))
        self.screen_rect = self.screen.get_rect()
        self.blue_bomber = BlueBomber()

    def run_game(self):
        while True:
            self.check_keypresses()
            self.blue_bomber.update_movement()
            self.screen.fill((122, 156, 245))
            self.blue_bomber.draw()
            pygame.display.flip()

    def check_keypresses(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.key_down(event)
            elif event.type == pygame.KEYUP:
                self.key_up(event)

    def key_down(self, event):
        if event.key == pygame.K_RIGHT:
            self.blue_bomber.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.blue_bomber.moving_left = True
        elif event.key == pygame.K_UP:
            self.blue_bomber.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.blue_bomber.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def key_up(self, event):
        if event.key == pygame.K_RIGHT:
            self.blue_bomber.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.blue_bomber.moving_left = False
        elif event.key == pygame.K_UP:
            self.blue_bomber.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.blue_bomber.moving_down = False


homework_game = Game()
homework_game.run_game()
