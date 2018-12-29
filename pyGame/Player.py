#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: Player.py
# @time: 2018/12/27 15:46
# @desc: 精灵模块

from random import randint
from sys import exit

import pygame
from pygame.locals import *

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640


# 声明Player类 继承自 pygame.sprite.Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, initial_position):
        # 父级构造函数
        pygame.sprite.Sprite.__init__(self)
        # 精灵图片Surface
        self.image = pygame.Surface([10, 10])
        self.image.fill((0, 0, 0))
        # 精灵图片的大小
        self.rect = self.image.get_rect()
        # 精灵图片的位置
        self.rect.topleft = initial_position

        self.speed = 6

    def update(self):
        self.rect.left += self.speed
        if self.rect.left > SCREEN_WIDTH:
            self.kill()


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# 建立精灵组
group = pygame.sprite.Group()

while True:
    clock.tick(10)
    print(len(group.sprites()))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # 绘制背景
    screen.fill((255, 255, 255))

    # 不断往精灵组中添加精灵
    group.add(Player((randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT))))

    # 将每个精灵更新后显示在Screen上
    group.update()
    group.draw(screen)
    pygame.display.update()
