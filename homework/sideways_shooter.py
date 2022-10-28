import sys
import pygame
from objects_sideways_shooter import SideShooter
from objects_sideways_shooter import Bullet

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        self.screen.fill((128, 0, 0))
        self.screen_rect = self.screen.get_rect()
        self.side_shooter = SideShooter()
        self.bullets = pygame.sprite.Group()


    def run_game(self):
        while True:
            self.screen.fill((128, 0, 0))
            self.check_keypresses()
            self.side_shooter.update_movement()
            self.bullets.update()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.side_shooter.draw()
            for bullet in self.bullets:
                if bullet.rect.right >= 400:
                    self.bullets.remove(bullet)
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



homework_game = Game()
homework_game.run_game()