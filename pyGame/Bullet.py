#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: Bullet.py
# @time: 2018/12/27 16:32
# @desc: 子弹类

import pygame

from StaticConfig import *


class Bullet(pygame.sprite.Sprite):
    # 子弹初始化方法,参数为子弹图片和初始化位置
    def __init__(self, bullet_init_pos):
        pygame.sprite.Sprite.__init__(self)
        # 设置子弹
        bullet_image = pygame.image.load(StaticConfig.BULLET_IMG)
        # 设置模型在子弹图片的位置大小
        bullet_rect = pygame.Rect(0, 0, 10, 14)
        self.image = bullet_image.subsurface(bullet_rect)
        self.rect = self.image.get_rect()
        self.rect.topleft = bullet_init_pos
        self.speed = 8

    # 子弹移动方法
    def update(self):
        self.rect.top -= self.speed
        if self.rect.top < -self.rect.height:
            self.kill()
