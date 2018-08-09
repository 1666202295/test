#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: ship.py
# @time: 2018/8/8 15:21
# @desc: 飞机类

import pygame


class Ship():
    def __init__(self, game_settings, screen):
        self.screen = screen
        self.game_settings = game_settings
        self.image = pygame.image.load("../resources/demoFile/image/灰机.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # buld the spaceship at the specific location
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
