#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: Enemy.py
# @time: 2018/12/27 20:03
# @desc: 敌人类

# 导入random库中的randint函数
from random import randint

import pygame

from StaticConfig import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # 设置敌人
        enemy_image = pygame.image.load(StaticConfig.ENEMY_IMG)
        # 设置模型在敌人图片的位置大小
        enemy_rect = pygame.Rect(0, 0, 40, 23)
        self.image = enemy_image.subsurface(enemy_rect)
        self.rect = self.image.get_rect()
        # 敌机的位置是从顶部开始随机位置开始的
        enemy_init_pos = [randint(0, StaticConfig.SCREEN_WIDTH - 20), 0]
        self.rect.topleft = enemy_init_pos
        # 移动速度
        self.speed = 2
        # 分数
        self.fraction = 1

    # 敌人移动方法
    def update(self):
        self.rect.top += self.speed
        if self.rect.top > StaticConfig.SCREEN_HEIGHT:
            self.kill()
