#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: gameFunctions.py
# @time: 2018/8/8 15:27
# @desc: 事件控制模块

import sys
import pygame
from settings import Bullet


# 按下键盘事件
def check_key_down_events(event, game_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # move right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # move right
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        # 按Q关闭
        sys.exit()


# 松开键盘事件
def check_key_up_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # move right
        ship.moving_left = False


# 游戏事件监控
def check_events(game_settings, screen, ship, bullets):
    # pygame.event.get() 创建当前等待处理的事件的一个列表
    # 理解为当前所有游戏事件的一个监听
    for event in pygame.event.get():
        # 如果时间的类型为退出
        if event.type == pygame.QUIT:
            # 关闭
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # 如果事件类型为按下键盘
            check_key_down_events(event, game_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            # 如果事件类型为松开键盘
            check_key_up_events(event, ship)


# 更新屏幕
def update_screen(game_settings, screen, ship, bullets, alien):
    # .fill 对surface对象填充某一种颜色，可以主要是对背景可以实现填充
    screen.fill(game_settings.bg_color)
    # 子弹更新
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()
    # 将整个display的surface对象更新到屏幕上去
    pygame.display.flip()


# 子弹开火事件
def fire_bullet(game_settings, screen, ship, bullets):
    """Fire a bullet, if limit not reached yet."""
    # Create a new bullet, add to bullets group.
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)


# 删除子弹事件
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
