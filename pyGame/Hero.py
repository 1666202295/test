#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: Hero.py
# @time: 2018/12/27 15:59
# @desc: 英雄角色类

# 导入pygame库
from Bullet import *


# 英雄角色类
class Hero(pygame.sprite.Sprite):

    # 英雄角色类初始化方法 传递参数 英雄图片 和 英雄角色的位置
    def __init__(self):
        # 父类初始化方法
        pygame.sprite.Sprite.__init__(self)
        # 设置英雄飞机
        shoot_img = pygame.image.load(StaticConfig.HERO_IMG)
        # 设置模型在飞机图片的位置大小
        hero_rect = pygame.Rect(0, 0, 50, 50)
        self.image = shoot_img.subsurface(hero_rect)
        self.rect = self.image.get_rect()
        # 英雄的位置
        self.rect.topleft = StaticConfig.HERO_POS
        # 英雄的移动变量
        self.speed = 6
        # 子弹组
        self.bullets = pygame.sprite.Group()
        # 英雄是否死亡 0 为未死亡
        self.is_hit = 0

    # 英雄移动方法
    def move(self, offset):
        right = offset[pygame.K_RIGHT]
        left = offset[pygame.K_LEFT]
        offset_x = right - left
        down = offset[pygame.K_DOWN]
        up = offset[pygame.K_UP]
        offset_y = down - up
        hero_x = self.rect.left + offset_x
        hero_y = self.rect.top + offset_y
        if hero_x < 0:
            self.rect.left = 0
        elif hero_x > StaticConfig.SCREEN_WIDTH - self.rect.width:
            self.rect.left = StaticConfig.SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left = hero_x

        if hero_y < 0:
            self.rect.top = 0
        elif hero_y > StaticConfig.SCREEN_HEIGHT - self.rect.height:
            self.rect.top = StaticConfig.SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top = hero_y

    # 射击行为
    def single_shoot(self):
        bullet = Bullet(self.rect.midtop)
        self.bullets.add(bullet)
