import sys
import pygame
from star_object import Star
from random import randint
class StarRun:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 700))
        self.screen.fill((0, 0, 0))
        self.stars = pygame.sprite.Group()
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((0,0,0))
            self.create_grid()
            self.stars.draw(self.screen)
            pygame.display.flip()
    def create_grid(self):
        star = Star()
        star_width = star.rect.width
        star_height = star.rect.height

        space_available_x = 700 - (2*star_width)
        stars_in_row = space_available_x // (2*star_width)

        space_available_y = 700 - (3 * star_height)
        number_of_rows = space_available_y // (2 * star_height)

        for row_number in range(number_of_rows):
            for star_number in range(stars_in_row):
                self.create_stars(star_number, row_number)
    def create_stars(self, star_number, row_number):
        star = Star()
        random_number = randint(-10,10)
        star_width = star.rect.width
        star_height = star.rect.height
        star.x = star_width + random_number * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star_height + random_number * star.rect.height * row_number
        self.stars.add(star)

test = StarRun()
test.run()

