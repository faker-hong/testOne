import pygame
from enum import Enum,unique
from math import sqrt
from random import randint
@unique
class Color(Enum):
    """��ɫ"""

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)
    @staticmethod
    def random_color():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)
class Ball(object):
    def __init__(self,x,y,radius,sx,sy,color=Color.RED):
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True
    def move(self,screen):
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or \
                self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or \
                self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        """��������"""
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        """�ڴ����ϻ�����"""
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)
def main():
    # ��������װ�����������
    balls = []
    # ��ʼ�������pygame�е�ģ��
    pygame.init()
    # ��ʼ��������ʾ�Ĵ��ڲ����ô��ڳߴ�
    screen = pygame.display.set_mode((800, 600))
    # ���õ�ǰ���ڵı���
    pygame.display.set_caption('�����С��')
    running = True
    # ����һ���¼�ѭ�����������¼�
    while running:
        # ����Ϣ�����л�ȡ�¼������¼����д���
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # ��������¼��Ĵ���
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # ��õ������λ��
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                # �ڵ������λ�ô���һ����(��С���ٶȺ���ɫ���)
                ball = Ball(x, y, radius, sx, sy, color)
                # ������ӵ��б�������
                balls.append(ball)
        screen.fill((255, 255, 255))
        # ȡ�������е��� ���û���Ե��ͻ��� ���Ե��˾��Ƴ�
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        # ÿ��50����͸ı����λ����ˢ�´���
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            # �������û�гԵ���������
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main()