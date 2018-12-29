#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: GameStart.py
# @time: 2018/12/27 16:23
# @desc: 程序启动类

from sys import exit

from Enemy import *
from Hero import *

# 英雄飞机1的移动变量
offset_one = {pygame.K_LEFT: 0, pygame.K_RIGHT: 0, pygame.K_UP: 0, pygame.K_DOWN: 0}
# # 英雄飞机2的移动变量
# offset_two = {pygame.K_w: 0, pygame.K_a: 0, pygame.K_d: 0, pygame.K_s: 0}

# 初始化游戏 初始化pygame
pygame.init()
# 初始化一个用于显示的窗口
screen = pygame.display.set_mode([StaticConfig.SCREEN_WIDTH, StaticConfig.SCREEN_HEIGHT])
# 设置窗口标题
pygame.display.set_caption(StaticConfig.WINDOWS_TITLE)
# 设置背景图
background = pygame.image.load(StaticConfig.BACK_GROUND)
# 创建英雄
hero_one = Hero()
# hero_two = Hero()
# pygame.time.Clock()帮我们创建一个记录时间的对象；
clock = pygame.time.Clock()

# 计数ticks
ticks = 0
# 计分
fraction_one = 0
# fraction_two = 0
# 敌人组
enemyGroups = pygame.sprite.Group()
# 敌人死亡组
enemyDownGroups_one = pygame.sprite.Group()
# enemyDownGroups_two = pygame.sprite.Group()
# 计分文本框
fontObj = pygame.font.Font("resource/otf/SourceHanSerifSC-Regular.otf", 32)
# 事件循环
while True:
    ticks += 1
    # clock.tick()就是限制游戏最大帧率（framerate）为60
    clock.tick(StaticConfig.FRAME_RATE)
    # screen.blit 第一个参数是源Surface对象，pos则是传送到screen的左上角的位置，是一个二元组，表示xy坐标
    # 绘制背景
    screen.blit(background, (0, 0))
    # 绘制飞机
    screen.blit(hero_one.image, hero_one.rect)
    # screen.blit(hero_two.image, hero_two.rect)
    # 绘制计分框
    fontObj_fmt = fontObj.render(str(fraction_one), 1, (10, 10, 10))
    # 绘制计分
    screen.blit(fontObj_fmt, (0, 0))

    if ticks % StaticConfig.BULLET_SPEED == 0:
        # 射击子弹
        hero_one.single_shoot()
        # hero_two.single_shoot()
    # 控制子弹
    hero_one.bullets.update()
    # hero_two.bullets.update()
    # 绘制子弹
    hero_one.bullets.draw(screen)
    # hero_two.bullets.draw(screen)
    if ticks % StaticConfig.ENEMY_ADD_SPEED == 0:
        # 产生敌人
        enemy = Enemy()
        enemyGroups.add(enemy)

    # 控制敌机
    enemyGroups.update()
    # 绘制敌机
    enemyGroups.draw(screen)

    # 监测敌机死亡
    # pygame.sprite.groupcollide() 方法为判定两个精灵模块是否发生碰撞 参数3表示是否杀掉精灵组1的元素 参数4表示是否杀死精灵组2的元素
    enemyDownGroups_one.add(pygame.sprite.groupcollide(enemyGroups, hero_one.bullets, True, True))
    # enemyDownGroups_two.add(pygame.sprite.groupcollide(enemyGroups, hero_two.bullets, True, True))
    for spritesItem in enemyDownGroups_one:
        fraction_one = fraction_one + spritesItem.fraction
    # for spritesItem in enemyDownGroups_two:
    #     fraction_two = fraction_two + spritesItem.fraction
    enemyDownGroups_one = pygame.sprite.Group()
    enemyDownGroups_two = pygame.sprite.Group()
    # 判断英雄是否发生碰撞
    hero_one_down_list = pygame.sprite.spritecollide(hero_one, enemyGroups, True)
    # hero_two_down_list = pygame.sprite.spritecollide(hero_two, enemyGroups, True)
    if len(hero_one_down_list) > 0:
        # 英雄发生碰撞
        hero_one.is_hit = 1
        shoot_hit_img = pygame.image.load(StaticConfig.HERO_HIT_IMG)
        hero_one.image = shoot_hit_img
        # 游戏结束图
        game_over_img = pygame.image.load(StaticConfig.GAME_OVER)
        screen.blit(game_over_img, (0, 0))
        # 更新屏幕
        pygame.display.update()
        break
    # if len(hero_two_down_list) > 0:
    #     # 英雄发生碰撞
    #     hero_two.is_hit = 1
    #     shoot_hit_img = pygame.image.load(StaticConfig.HERO_HIT_IMG)
    #     hero_two.image = shoot_hit_img
    #     # 游戏结束图
    #     game_over_img = pygame.image.load(StaticConfig.GAME_OVER)
    #     screen.blit(game_over_img, (0, 0))
    #     # 更新屏幕
    #     pygame.display.update()
    #     break
    # 从消息队列中循环取出事件
    for event in pygame.event.get():
        # 处理退出事件
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # 是否为按下动作
        if event.type == pygame.KEYDOWN:
            # 按键是否在英雄移动参数内
            if event.key in offset_one:
                # 对应属性移动值为3
                offset_one[event.key] = 3
            # # 按键是否在英雄移动参数内
            # if event.key in offset_two:
            #     # 对应属性移动值为3
            #     offset_two[event.key] = 3
        # 是否为松开动作
        elif event.type == pygame.KEYUP:
            if event.key in offset_one:
                offset_one[event.key] = 0
            # if event.key in offset_two:
            #     offset_two[event.key] = 3
    # 英雄移动
    hero_one.move(offset_one)
    # hero_two.move(offset_two)
    # 更新屏幕
    pygame.display.update()
