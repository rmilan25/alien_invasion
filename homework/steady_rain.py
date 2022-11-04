import sys
import pygame
from star_object import Star


class StarRun:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 700))
        self.screen.fill((0, 0, 0))
        self.stars = pygame.sprite.Group()
        self.create_grid()
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((0, 0, 0))
            self.stars.draw(self.screen)
            self.move_stars()
            self.check_star_edge()
            pygame.display.flip()

    def create_grid(self):
        star = Star(self.screen)
        star_width = star.rect.width
        star_height = star.rect.height

        space_available_x = 700 - (2 * star_width)
        stars_in_row = space_available_x // (2 * star_width)

        space_available_y = 700 - (3 * star_height)
        number_of_rows = space_available_y // (2 * star_height)

        for row_number in range(number_of_rows):
            for star_number in range(stars_in_row):
                self.create_stars(star_number, row_number)

    def create_stars(self, star_number, row_number):
        star = Star(self.screen)
        star_width = star.rect.width
        star_height = star.rect.height
        star.rect.x = star_width + 2 * star_width * star_number
        star.rect.y = star_height + 2 * star.rect.height * row_number
        self.stars.add(star)

    def move_stars(self):
        self.stars.update()

    def check_star_edge(self):
        for star in self.stars.sprites():
            if star.rect.y < 700:
                return True
        if self.stars.sprites():
            self.create_grid()
            print('created grid')


test = StarRun()
test.run()
