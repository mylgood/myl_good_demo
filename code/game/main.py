import pygame
import  random
from pygame.locals import *

# 窗体的高度和宽度
WIDTH = 1200
HEIGHT = 600


# 豌豆对象
class Peas:
    def __init__(self):
        self.image = pygame.image.load("./res/peas.gif")
        self.image_rect = self.image.get_rect()
        self.image_rect.top = 280
        self.image_rect.left = 30
        # 设置豌豆是否向下移动
        self.is_move_down = False
        self.is_move_up = False
        self.is_shout = False

    def display(self):
        """豌豆显示在页面上"""
        screen.blit(self.image, self.image_rect)

    def move_up(self):
        if self.image_rect.top > 20:
            self.image_rect.move_ip(0, -6)
        for z in Zombie.zombie_list:
            if self.image_rect.colliderect(z.image_rect):
                pygame.quit()
                exit()

    def move_down(self):
        if self.image_rect.bottom < 600:
            self.image_rect.move_ip(0, 6)
        for z in Zombie.zombie_list:
            if self.image_rect.colliderect(z.image_rect):
                pygame.quit()
                exit()

    def shout_bullet(self):
        # 创建一个炮弹对象
        bullet = Bullet(self)
        # 保存创建好的炮弹对象
        Bullet.bullet_list.append(bullet)


# 炮弹对象
class Bullet:
    # 显示所有的炮弹信息
    bullet_list=[]
    # 炮弹的间隔时间
    interval = 0

    def __init__(self, pea):
        self.image = pygame.image.load("./res/bullet.gif")
        self.image_rect = self.image.get_rect()
        self.image_rect.top = pea.image_rect.top
        self.image_rect.left = pea.image_rect.right

    def display(self):
        """炮弹显示在页面上"""
        screen.blit(self.image, self.image_rect)

    def move(self):
        self.image_rect.move_ip(10, 0)
        # 如果炮弹越界,删除炮弹
        if self.image_rect.left > WIDTH - 10:
            Bullet.bullet_list.remove(self)
        for z in Zombie.zombie_list:
            if self.image_rect.colliderect(z.image_rect):
                Bullet.bullet_list.remove(self)
                Zombie.zombie_list.remove(z)
                break


# 僵尸对象
class Zombie:
    # 创建频率
    interval = 0
    # 保存多个僵尸
    zombie_list = []

    def __init__(self):
        self.image = pygame.image.load("./res/zombie.gif")
        # 改变图片大小
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.image_rect = self.image.get_rect()
        self.image_rect.top = random.randint(10, HEIGHT-70)
        self.image_rect.left = WIDTH

    def display(self):
        """僵尸显示在页面上"""
        screen.blit(self.image, self.image_rect)

    def move(self):
        """僵尸移动"""
        self.image_rect.move_ip(-2, 0)
        if self.image_rect.right <= 0:
            Zombie.zombie_list.remove(self)
        for b in Bullet.bullet_list:
            if self.image_rect.colliderect(b.image_rect):
                Zombie.zombie_list.remove(self)
                Bullet.bullet_list.remove(b)
                break
        if self.image_rect.colliderect(peas.image_rect):
            pygame.quit()
            exit()


def key_control():
    """事件监听处理"""
    for event in pygame.event.get():
        # 事件类型判断
        if event.type == QUIT:
            pygame.quit()
            exit()
        # 按下事件类型的监听
        elif event.type == KEYDOWN:
            # 判断具体的键
            if event.key == K_UP:
                peas.is_move_up = True
            elif event.key == K_DOWN:
                peas.is_move_down = True
            elif event.key == K_SPACE:
                peas.is_shout = True
        elif event.type == KEYUP:
            # 判断具体的键
            if event.key == K_UP:
                peas.is_move_up = False
            elif event.key == K_DOWN:
                peas.is_move_down = False
            elif event.key == K_SPACE:
                peas.is_shout = False


if __name__ == '__main__':
    # 显示窗体
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # 背景图片
    background_image = pygame.image.load("./res/background.png")
    # 改变图片大小
    scale_background_image = pygame.transform.scale(background_image,(WIDTH,HEIGHT))
    # 获取到图片的位置和大小
    scale_background_image_rect = scale_background_image.get_rect()
    # 创建一个时钟, 优化运行的速度效果
    clock = pygame.time.Clock()
    # 创建一个豌豆对象
    peas = Peas()
    while True:
        # 设置背景颜色为黑色
        screen.fill((0, 0, 0))
        # 设置窗体的背景图片
        screen.blit(scale_background_image, scale_background_image_rect)
        # 显示豌豆
        peas.display()
        # 对事件的处理
        key_control()
        if peas.is_move_up:
            peas.move_up()
        if peas.is_move_down:
            peas.move_down()
        # 发射炮弹
        Bullet.interval += 1
        if peas.is_shout and Bullet.interval >= 20:
            Bullet.interval = 0
            peas.shout_bullet()

        Zombie.interval += 1
        if Zombie.interval >= 20:
            Zombie.interval = 0
            # 创建僵尸对象 并且保存起来
            zombie = Zombie()
            Zombie.zombie_list.append(zombie)
        # 帧频率
        # 显示所有的炮弹
        for bullet in Bullet.bullet_list:
            # 炮弹显示
            bullet.display()
            #炮弹移动
            bullet.move()

        for zombie in Zombie.zombie_list:
            # 显示僵尸
            zombie.display()
            # 僵尸移动
            zombie.move()
        clock.tick(60)
        # 显示图片
        pygame.display.update()


