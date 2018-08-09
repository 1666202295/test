#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: settings.py.py
# @time: 2018/8/8 14:59
# @desc: 游戏配置类

import pygame
from pygame.sprite import Sprite


class Settings(object):
    def __init__(self):
        # 窗体宽度
        self.screen_width = 1200
        # 窗体高度
        self.screen_height = 800
        # 窗体背景色
        self.bg_color = (230, 230, 230)
        # 模型移动速度
        self.ship_speed_factor = 1.5
        # 子弹总量
        self.bullets_allowed = 3
        # 子弹宽度
        self.bullet_width = 3
        # 子弹高度
        self.bullet_height = 15
        # 子弹颜色
        self.bullet_color = 60, 60, 60
        # 子弹速度
        self.bullet_speed_factor = 3
        # 敌人速度
        self.alien_speed_factor = 1

        # Scoring.
        self.alien_points = 50

        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1


# 子弹
class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, game_settings, screen, ship):
        """Create a bullet object, at the ship's current position."""
        super().__init__()
        self.screen = screen

        # Create bullet rect at (0, 0), then set correct position.
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width,
                                game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store a decimal value for the bullet's position.
        self.y = float(self.rect.y)

        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)


# 外星人
class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien, and set its starting position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image, and set its rect attribute.
        self.image = pygame.image.load('../resources/demoFile/image/敌机.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width + self.rect.x
        self.rect.y = self.rect.height + self.rect.y

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
