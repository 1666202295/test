#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: BulletReward.py
# @time: 2018/12/28 17:45
# @desc: 子弹奖励(升级类)

import pygame


class Bullet(pygame.sprite.Sprite):
    # 子弹初始化方法,参数为子弹图片和初始化位置
    def __init__(self,bullet_init_pos):
        pygame.sprite.Sprite.__init__(self)


