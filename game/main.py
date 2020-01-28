import pygame
import random
from pygame.locals import *


# 设置窗口的宽度
WIDTH = 1200
# 设置窗口的高度
HEIGHT = 600


# 定义一个豌豆对象
class Peas:
    # 初始化方法
    def __init__(self):
        # 加载一个豌豆图片
        self.image = pygame.image.load("./res/peas.gif")
        # 获取到豌豆图片的大小和位置
        self.image_rect = self.image.get_rect()
        # 设置豌豆显示的位置
        self.image_rect.top = 285
        self.image_rect.left = 30
        # 判断豌豆是否向上移动
        self.is_move_up = False
        # 判断豌豆是否向下移动
        self.is_move_down = False
        # 判断豌豆是否射炮弹
        self.is_shout = False

    def display(self):
        """显示豌豆的方法"""
        screen.blit(self.image, self.image_rect)

    def move_up(self):
        """豌豆向上移动"""
        if self.image_rect.top > 30:
            # move_ip 可以改变图片的显示对x,y的坐标位置
            self.image_rect.move_ip(0, -10)
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
        # 创建一个炮弹
        bullet = Bullet(self)
        Bullet.bullet_list.append(bullet)

# 定义炮弹对象
class Bullet:
    # 所有的炮弹信息
    bullet_list = []
    # 创建炮弹间隔
    interval = 0

    def __init__(self, peas):
        # 加载一个豌豆图片
        self.image = pygame.image.load("./res/bullet.gif")
        # 获取到豌豆图片的大小和位置
        self.image_rect = self.image.get_rect()
        # 设置豌豆显示的位置
        self.image_rect.top = peas.image_rect.top
        self.image_rect.left = peas.image_rect.right

    def display(self):
        """显示炮弹的方法"""
        screen.blit(self.image, self.image_rect)

    def move(self):
        """移动炮弹"""
        self.image_rect.move_ip(8, 0)
        if self.image_rect.right > WIDTH - 20:
            Bullet.bullet_list.remove(self)
        else:
            for z in Zombie.zombie_list[:]:
                if self.image_rect.colliderect(z.image_rect):
                    Zombie.zombie_list.remove(z)
                    Bullet.bullet_list.remove(self)
                    break


class Zombie:
    # 所有的僵尸信息
    zombie_list = []
    # 创建炮弹间隔
    interval = 0

    def __init__(self):
        # 加载一个豌豆图片
        self.image = pygame.image.load("./res/zombie.gif")
        self.image = pygame.transform.scale(self.image, (70, 70))
        # 获取到豌豆图片的大小和位置
        self.image_rect = self.image.get_rect()
        # 设置豌豆显示的位置
        self.image_rect.top = random.randint(10, HEIGHT-70)
        self.image_rect.left = WIDTH

    def display(self):
        """显示炮弹的方法"""
        screen.blit(self.image, self.image_rect)

    def move(self):
        """移动僵尸"""
        self.image_rect.move_ip(-2, 0)
        if self.image_rect.left < 0:
            Zombie.zombie_list.remove(self)
        else:
            # 撞到豌豆
            if self.image_rect.colliderect(peas.image_rect):
                pygame.quit()
                exit()
            for b in Bullet.bullet_list[:]:
                if self.image_rect.colliderect(b.image_rect):
                    Bullet.bullet_list.remove(b)
                    Zombie.zombie_list.remove(self)
                    break

# 键盘控制事件监听抽取
def key_control():
    # 获取到所有的事件
    for event in pygame.event.get():
        # 如果事件类型是退出, 点击关闭按钮
        if event.type == QUIT:
            # 退出pygame
            pygame.quit()
            # 退出程序
            exit()
        # 事件类型是键盘按下
        if event.type == KEYDOWN:
            # 向下键
            if event.key == K_UP:
                # 设置豌豆的移动方向
                peas.is_move_up = True
                peas.is_move_down = False
            elif event.key == K_DOWN:
                peas.is_move_up = False
                peas.is_move_down = True
            elif event.key == K_SPACE:
                peas.is_shout = True
        # 事件类型是键盘松开
        if event.type == KEYUP:
            if event.key == K_UP:
                peas.is_move_up = False
            elif event.key == K_DOWN:
                peas.is_move_down = False
            elif event.key == K_SPACE:
                peas.is_shout = False


if __name__ == '__main__':
    # 初始化pygame
    pygame.init()
    # 显示界面  窗口的大小
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # 设置背景图片
    background_image = pygame.image.load("./res/background.png")
    # 调整背景图片大小 设置和窗口一样大小
    scale_background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    # 获取到背景图片的位置和大小 (x,y,width,height) 矩形区域
    scale_background_image_rect = scale_background_image.get_rect()
    # 定义一个时钟对象
    clock = pygame.time.Clock()
    # 创建一个豌豆对象
    peas = Peas()
    while True:
        # 设置背景颜色为黑色
        screen.fill((0,0,0))
        # 设窗口设置背景图片
        screen.blit(scale_background_image, scale_background_image_rect)
        peas.display()
        key_control()
        if peas.is_move_up:
            peas.move_up()
        if peas.is_move_down:
            peas.move_down()
        # 每隔20次发送一个炮弹
        Bullet.interval += 1
        if peas.is_shout and Bullet.interval >= 15:
            Bullet.interval = 0
            peas.shout_bullet()

        # 每隔一段时间创建炮弹
        Zombie.interval += 1
        if Zombie.interval >= 15:
            Zombie.interval = 0
            Zombie.zombie_list.append(Zombie())

        for bullet in Bullet.bullet_list:
            # 显示炮弹
            bullet.display()
            # 移动炮弹
            bullet.move()

        for zombie in Zombie.zombie_list:
            zombie.display()
            zombie.move()
        # 重新显示窗口 显示图片
        pygame.display.update()
        clock.tick(60)
