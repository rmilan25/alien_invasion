import sys
import pygame

class Keys:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((200, 200))

    def run_test(self):
        while True:
            self.screen.fill((0, 0, 255))
            self.check_keypresses()
            pygame.display.flip()
    def check_keypresses(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(pygame.KEYDOWN)

test = Keys()
test.run_test()