外星人入侵设计思路

一、武装飞船ship

    1.规划项目
        玩家控制一艘屏幕底端中央的飞船，使用左右箭头进行移动，使用空格键进行射击上方游动的一群外星人。外星人先向右移动，
        到右边界再向左移动同时向下移动一点，如此反复移动，直到外星人撞击了飞船或外星人抵达了屏幕底端，飞船损失一艘。
        玩家将所有外星人射杀完后会出现一群新的外星人，并且移动速度比上一群快，以此类推，玩家消灭外星人或有得分score与
        等级level，在屏幕右上端显示，屏幕顶端中央显示最高得分high_score，玩家损失三艘飞船，游戏结束。

    2.安装Pygame  使用 pip install Pygame

    3.开始游戏项目
        1.创建Pygame窗口以及响应用户输入    alien_invasion.py
        2.设置背景色 bg_color = (230, 230, 230) --> 浅灰色
        3.创建设置类 Settings 所有的游戏设置

    4.添加飞船图像    使用位图（bmp格式）
        1.创建ship类
        2.在屏幕上绘制飞船

    5.重构：模块game_functions

    6.驾驶飞船
        1.响应按键
        2.允许不断移动
        3.左右移动
        4.调整飞船的速度
        5.限制飞船的活动范围（不让飞船移出设置的屏幕）
        6.重构check_events()
        7.射击
            1.添加子弹设置
            2.创建Bullet类
            3.将子弹存储到编组中
            4.开火
            5.删除已消失的子弹
            6.限制子弹数量
            7.创建函数update_bullets()

二、创建外星人alien

    1.在游戏功能中，添加
        elif event.key = pygame.K_q
            sys.exit()
        使用户按Q键即可退出游戏，无需操作鼠标

    2. 创建第一个外星人
        1.创建Alien类
        2.创建Alien实例
        3.让外星人出现在屏幕上

    3.创建一群外星人
        1.确定一行可容纳多少个外星人
            available_space_x = ai_settings.screen.screen_width - (2 * alien_width)
            number_aliens_x = available_space_x / (2 * alien_width)
        2.创建多行外星人
        3.创建外星人群
        4.重构create_fleet()
        5.添加多行外星人

    4.让外星人群移动
        1.向右移动外星人（移到右边界便消失）
        2.创建表示外星人移动方向的设置（移到右边界向下移动、再向左移动）：外星人移动只有两种可能，使用数字1增大x，-1减小x
        3.检查外星人是否撞到了屏幕边缘
        4.向下移动外星人群并改动移动方向（设置完外星人群会向右移动，碰到边界向下一点再向左，不断重复这样的循环进行移动）

    5.射杀外星人
        1.检测子弹与外星人的碰撞 pygame.sprite.groupcollide() 传递四个参数，两个碰撞的游戏元素、两个元素碰撞后是否消失
        2.为测试创建大子弹（将bullet_width设置成大的值 或 bullets的属性设为False[表示子弹到屏幕顶端才消失]）
        3.生成新的外星人群（消灭一群又显示一群）
        4.提高子弹的速度 bullet_speed_factor
        5.重构update_bullets()

    6.结束游戏
        1.检测外星人和飞船碰撞
        2.响应外星人和飞船碰撞（统计碰撞次数、使用time.sleep()暂停一会让玩家可以看到，碰撞后清空子弹和外星人，“新飞船”(其实还是那条飞船)居中在屏幕底端）
        3.有外星人到达屏幕底端（当外星人到达屏幕底端的处理结果跟外星人与飞船相撞一样，都调用ship_hit()方法）
        4.游戏结束（之前设置的飞船数=3，小于1后为0，之后会变成负数导致游戏无法结束，因此设置个属性，为0时游戏结束）

    7.确定应运行游戏的哪些部分（哪些部分不受上边游戏属性限制会一直执行以及上边的游戏属性活跃时执行不活跃时不执行）

三、记分

    1.添加Play按钮（用于根据需要启动游戏以及游戏结束后重启游戏）
        1.创建Button类（创建带标签的实心矩形）
        2.在屏幕上绘制按钮（在屏幕更新时显示按钮）
        3.开始游戏（监视Play按钮相关鼠标事件，以在玩家单击Play按钮时开始新游戏）
        4.重置游戏（处理游戏结束的情况[重置统计信息、删除现有的外星人和子弹、创建一群新外星人、飞船居中]，玩家点击Play按钮可以重新开始游戏）
        5.将Play按钮切换到非活动状态（游戏开始后玩家点击Play按钮会重新开始游戏，修复这个问题可让game_active为False时才开始
        6.隐藏光标（在游戏处于活动状态时让光标不可见set_visible(False)

    2.提高等级
        1.修改速度设置 speedup_scale控制游戏节奏的加快速度（原速度 *= speedup_scale：1为原速度，2为原速度的2倍）
        2.重置速度（玩家开始新游戏时重置原来的速度）

    3.记分（实现一个记分系统，实时跟踪玩家的得分，并显示最高得分。当前等级和余下的飞船数）
        1.显示记分（创建记分的类，渲染到屏幕上一幅图像）
        2.创建记分牌（显示得分）
        3.在外星人消灭时更新得分（指定击中一个外星人多少分，实时显示得分，每当外星人被击中时更新stats.score的值，再调用prep_score()更新得分图像）
        4.将消灭的每个外星人的点数都计入得分（修复遗漏的每个外星人，都加分：调整检测子弹和外星人碰撞的方式）
        5.提高点数（等级越高，外星人点数越大）
        6.将得分圆整（显示为10的整数倍round(score, -1)，并添加逗号表示千位分隔符 "{:,}".format(score)
        7.最高得分(在任何情况下都不应重置最高得分；每当有外星人消灭时都要比较当前得分与最高得分，当前得分高则更新)
        8.显示等级（在游戏中显示玩家的等级）  格式化输出字符串 -->  "{:,}".format()
        9.显示余下的飞船数

# py文件说明：
    alien_invasion.py
        创建游戏用到的对象、游戏的主循环，玩此游戏的运行文件
    settings.py
        包含Settings类，只包含方法__init__()，初始化游戏外观、飞船速度的属性
    game_function.py
        包含一系列函数，执行游戏大部分工作
    ship.py
        包含Ship类，该类包含方法__init__()、管理飞船位置的方法update()、在屏幕上绘制飞船的方法blitme()
        飞船图像的加载