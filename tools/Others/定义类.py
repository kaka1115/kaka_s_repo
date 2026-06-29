# 定义一个“手机类”（模板）
class Phone:
    # 1. 属性：定义手机的基础数据（通过__init__初始化）
    def __init__(self, brand, screen_size, battery):
        self.brand = brand  # 品牌（比如“苹果”）
        self.screen_size = screen_size  # 屏幕尺寸（比如6.1英寸）
        self.battery = battery  # 电量（比如100%）

    # 2. 行为：定义对属性的操作（函数）
    def call(self, number):  # 打电话（操作“号码”，不直接改手机属性）
        print(f"用{self.brand}手机给{number}打电话")

    def charge(self, add):  # 充电（修改“电量”属性）
        self.battery = min(self.battery + add, 100)  # 电量不超过100%
        print(f"充电后，电量为{self.battery}%")


# 用“手机类”创建具体的手机（称为“对象”或“实例”）
my_phone = Phone("苹果", 6.1, 50)  # 实例1：我的苹果手机，初始电量50%
your_phone = Phone("华为", 6.7, 80)  # 实例2：你的华为手机，初始电量80%

# 调用对象的行为
my_phone.call("13800138000")  # 输出：用苹果手机给13800138000打电话
my_phone.charge(30)  # 输出：充电后，电量为80%