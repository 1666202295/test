#!/usr/bin/env python
# encoding: utf-8
# @author: 曹会金
# @license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
# @contact: deamoncao100@gmail.com
# @software: garner
# @file: Config.py
# @time: 2018/12/27 16:53
# @desc: 信息配置类


class StaticConfig:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass


# 定义窗体的分辨率
# 游戏窗体 宽
StaticConfig.SCREEN_WIDTH = 470
# 游戏窗体 高
StaticConfig.SCREEN_HEIGHT = 600
# 敌人产生的速度
StaticConfig.ENEMY_ADD_SPEED = 1
# 子弹产生的速度
StaticConfig.BULLET_SPEED = 10
# 游戏窗体标题
StaticConfig.WINDOWS_TITLE = "joker game"
# 游戏背景图片路径
StaticConfig.BACK_GROUND = "resource/img/backGround.jpg"
# 游戏画面帧率
StaticConfig.FRAME_RATE = 60
# 游戏结束背景图
StaticConfig.GAME_OVER = "resource/img/gameOver.png"

# 英雄图片路径
StaticConfig.HERO_IMG = "resource/img/shoot.png"
StaticConfig.HERO_HIT_IMG = "resource/img/shoot_hit.png"
# 英雄初始化位置
StaticConfig.HERO_POS = [215, 500]

# 子弹图片路径
StaticConfig.BULLET_IMG = "resource/img/bullet.png"

# 敌人图片路径
StaticConfig.ENEMY_IMG = "resource/img/enemy.png"
