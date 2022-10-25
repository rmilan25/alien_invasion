import pygame
import time

screen = pygame.display.set_mode((200,200))
screen.fill((122,156,245))
screen_rect = screen.get_rect()

blue_bomber = pygame.image.load('../images/blue_bomber.png')
rect = blue_bomber.get_rect()
rect.center = screen_rect.center
screen.blit(blue_bomber,rect)
pygame.display.flip()

time.sleep(4)
