import sys
import pygame
import time
from objects_sideways_shooter import SideShooter
from objects_sideways_shooter import Bullet
from objects_sideways_shooter import Invader

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 700))
        self.screen.fill((128, 0, 0))
        self.screen_rect = self.screen.get_rect()
        self.side_shooter = SideShooter()
        self.bullets = pygame.sprite.Group()
        self.invaders = pygame.sprite.Group()
        self.create_grid()
        self.ship_limit = 3
        self.game_active = True
    def run_game(self):
        while True:
            self.check_keypresses()
            if self.game_active:
                self.screen.fill((128, 0, 0))
                self.side_shooter.update_movement()
                self.bullets.update()
                for bullet in self.bullets.sprites():
                    bullet.draw_bullet()
                self.side_shooter.draw()
                self.invaders.draw(self.screen)
                for bullet in self.bullets:
                    if bullet.rect.right >= 700:
                        self.bullets.remove(bullet)
                self.move_invaders()
                self.check_invaders_x_edge()
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
        if event.key == pygame.K_UP:
            self.side_shooter.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.side_shooter.moving_down = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def key_up(self, event):
        if event.key == pygame.K_UP:
            self.side_shooter.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.side_shooter.moving_down = False

    def fire_bullet(self):
        new_bullet = Bullet(homework_game)
        self.bullets.add(new_bullet)
        collisions = pygame.sprite.groupcollide(self.bullets, self.invaders, True, True)
        if not self.invaders:
            self.bullets.empty()
            self.create_grid()

    def create_invaders(self, invader_number, row_number):
        invader = Invader(self.screen)
        invader_width = invader.rect.width
        invader_height = invader.rect.height
        invader.rect.x = 300 + 2 * invader_width * invader_number
        invader.rect.y = invader_height + 2 * invader.rect.height * row_number
        self.invaders.add(invader)

    def create_grid(self):
        invader = Invader(self.screen)
        invader_width = invader.rect.width
        invader_height = invader.rect.height

        space_available_x = 450 - (2 * invader_width)
        invaders_in_row = space_available_x // (2 * invader_width)

        space_available_y = 700 - (3 * invader_height)
        number_of_rows = space_available_y // (2 * invader_height)

        for row_number in range(number_of_rows):
            for invader_number in range(invaders_in_row):
                self.create_invaders(invader_number, row_number)

    def check_invaders_x_edge(self):
        for invader in self.invaders.sprites():
            if invader.rect.x > 0:
                return True
        if self.invaders.sprites():
            self.invaders.empty()
            self.create_grid()

    def side_shooter_hit(self):
        if self.ship_limit > 0:
            self.ship_limit -= 1
            self.invaders.empty()
            self.bullets.empty()
            self.create_grid()
            self.side_shooter.draw()
            print(self.ship_limit)
            time.sleep(1)
        else:
            self.game_active = False
            print('Game Over')

    def move_invaders(self):
        self.invaders.update()
        if pygame.sprite.spritecollideany(self.side_shooter, self.invaders):
            self.side_shooter_hit()





homework_game = Game()
homework_game.run_game()