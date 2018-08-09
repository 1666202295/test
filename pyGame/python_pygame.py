#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: python_pygame.py
# @time: 2018/8/8 14:18
# @desc: pygame 是python 开发游戏的模块

import pygame
from settings import Settings
from ship import Ship
import gameFunctions as gf
from pygame.sprite import Group
from settings import Alien


def run_game():
    # pygame 模块初始化
    pygame.init()
    game_settings = Settings()
    # 构建窗口 生成windows窗口 返回一个surface对象
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    ship = Ship(game_settings, screen)
    alien = Alien(game_settings, screen)
    # 子弹
    bullets = Group()
    pygame.display.set_caption("first game")

    # 游戏循环
    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        bullets.update()
        # 删除子弹
        gf.update_bullets(bullets)
        gf.update_screen(game_settings, screen, ship, bullets, alien)
        ship.update()


run_game()
