import pygame
import random
from pygame.locals import *

WIDTH = 1200
HEIGHT = 600

class Peas:
    def __init__(self):
        self.image = pygame.image.load("./res/peas.gif")
        self.image_rect = self.image.get_rect()
        self.image_rect.top = 285
        self.image_rect.left = 30
        self.is_move_up = False
        self.is_move_down = False
        self.is_shout = False

    def display(self):
        """显示豌豆的方法"""
        screen.blit(self.image,self.image_rect)

    def move_up(self):
        """豌豆向上移动"""
        if self.image_rect.top > 30:
            self.image_rect.move_ip(0,-10)
        else:
            for z in Zombie.zombie_list:
                if self.image_rect.colliderect(z.image_rect):
                    pygame.quit()
                    exit()

    def move_down(self):
        """豌豆向下移动"""
        if self.image_rect.bottom < HEIGHT - 10:
            self.image_rect.move_ip(0, 10)
        else:
            for z in Zombie.zombie_list:
                if self.image_rect.colliderect(z.image_rect):
                    pygame.quit()
                    exit()

    def shout_bullet(self):
        """发射炮弹方法"""
        bullet = Bullet(self)
        Bullet.bullet_list.append(bullet)

class Bullet:
    bullet_list = []
    interval = 0
    def __init__(self,peas):
        self.image = pygame.image.load("./res/bullet.gif")
        self.image_rect = self.image.get_rect()
        self.image_rect.top = peas.image_rect.top
        self.image_rect.left = peas.image_rect.right

    def display(self):
        """显示炮弹的方法"""
        screen.blit(self.image,self.image_rect)

    def move(self):
        """移动炮弹"""
        self.image_rect.move_ip(8,0)
        if self.image_rect.right > WIDTH - 20:
            Bullet.bullet_list.remove(self)
        else:
            for z in Zombie.zombie_list[:]:
                if self.image_rect.colliderect(z.image_rect):
                    Zombie.zombie_list.remove(z)
                    Bullet.bullet_list.remove(self)
                    break

class Zombie:
    zombie_list = []
    interval=0

    def __init__(self):
        self.image = pygame.image.load("./res/zombie.gif")
        self.image = pygame.transform.scale(self.image,(70,70))
        self.image_rect = self.image.get_rect()
        self.image_rect.top = random.randint(10,HEIGHT-70)
        self.image_rect.left = WIDTH

    def display(self):
        """显示炮弹的方法"""
        screen.blit(self.image,self.image_rect)

    def move(self):
        """移动僵尸"""
        self.image_rect.move_ip(-2,0)
        if self.image_rect.left < 0:
            Zombie.zombie_list.remove(self)
        else:
            if self.image_rect.colliderect(peas.image_rect):
                pygame.quit()
                exit()
            for b in Bullet.bullet_list[:]:
                if self.image_rect.colliderect(b.image_rect):
                    Bullet.bullet_list.remove(b)
                    Zombie.zombie_list.remove(self)
                    break


def key_control():

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                peas.is_move_up = True
                peas.is_move_down = False
            elif event.key == K_DOWN:
                peas.is_move_up = False
                peas.is_move_down = True
            elif event.key == K_SPACE:
                peas.is_shout = True
        if event.type == KEYUP:
            if event.key == K_UP:
                peas.is_move_up = False
            elif event.key == K_DOWN:
                peas.is_move_down = False
            elif event.key == K_SPACE:
                peas.is_shout = False

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    background_image = pygame.image.load("./res/background.png")
    scale_background_image = pygame.transform.scale(background_image,(WIDTH,HEIGHT))
    scale_background_image_rect = scale_background_image.get_rect()
    clock = pygame.time.Clock()
    peas = Peas()
    while True:
        screen.fill((0,0,0))
        screen.blit(scale_background_image,scale_background_image_rect)
        peas.display()
        key_control()
        if peas.is_move_up:
            peas.move_up()
        if peas.is_move_down:
            peas.move_down()
        Bullet.interval += 1
        if peas.is_shout and Bullet.interval >= 15:
            Bullet.interval = 0
            peas.shout_bullet()
        Zombie.interval += 1
        if Zombie.interval >= 15:
            Zombie.interval = 0
            Zombie.zombie_list.append(Zombie())
        for bullet in Bullet.bullet_list:
            bullet.display()
            bullet.move()

        for zombie in Zombie.zombie_list:
            zombie.display()
            zombie.move()
        pygame.display.update()
        clock.tick(60)








