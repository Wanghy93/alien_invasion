"""外星人入侵游戏"""
# 要玩游戏《外星人入侵》，只需运行这个py文件即可
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()  # ai_settings继承Settings类的属性和方法
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮（游戏需要玩家点击“Play”才能开始）
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)

    # 创建一艘飞船（实例）
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个外星人编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 设置背景色
    bg_color = (230, 230, 230)

    # 创建一个外星人
    alien = Alien(ai_settings, screen)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)  # 主循环检查玩家的输入
        if stats.game_active:
            ship.update()  # 更新飞船的位置（每次循环都可以调用飞船的响应按键和鼠标操作的方法，即左右移动）
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)  # 子弹的位置和删除已消失的子弹 + 外星人的位置和删除与子弹重叠的外星人
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        # 先绘制飞船和子弹，再绘制外星人，让外星人在屏幕上位于最前面
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)  # 更新后的位置绘制新屏幕


run_game()
