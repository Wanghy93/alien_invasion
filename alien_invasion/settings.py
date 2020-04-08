class Settings():
    """存储《外星人入侵》的所有设置的类，初始化控制游戏外观和飞船速度的属性"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5  # 飞船移动速度由1像素改为1.5像素
        self.ship_limit = 3  # 玩家拥有飞船的数量（就是有几条命）

        # 子弹设置
        self.bullet_speed_factor = 2  # 子弹的速度
        self.bullet_width = 3  # 宽 3 像素
        self.bullet_height = 15  # 高 15 像素
        self.bullet_color = 60, 60, 60  # 深灰色
        self.bullets_allowed = 5  # 允许屏幕上最多出现 5 发子弹

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，-1表示向左移
        self.fleet_direction = 1

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1  # 游戏难度的调节值
        # 外星人点数(得分)的提高速度
        self.score_scale = 1.5  # scale 规模、比例

        self.initialize_dynamic_settings()  # 初始化随游戏进行而变化的属性

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction = 1

        # 记分（击中一个外星人多少分）
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置和外星人点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)   # 使用int使点数为整数
        # print(self.alien_points)  # 每消灭一群外星人，都会打印一个新的点数值
