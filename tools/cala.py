# 计算拖带阻力 resistance calculation
# 设置两个个字典来装拖轮和被拖船的参数，键值对，它和列表的区别就是键值对。
tow_data = {
    'length': 78,
    'b': 36,
    'd': 4,
    'v': 2.57,
    'o': 1
}

tug_data = {
    'length': 59.25,
    'b': 14.95,
    'd': 4,
    'v': 2.57,
    'o': 1
}
# 定义一个总的函数公式  #定义函数前面应该有两个空行，定义后也应该有两个空行。


def f(length, b, d, v, o):
    return 1.15 * ((1.67 * length * (1.7 * d + o * b) * v**1.83 * 0.001) +
                   (0.147 * o * (o * b * d) * v**(1.74 + 0.15 * v)))


tow_Resistance = f(tow_data['length'], tow_data['b'], tow_data['d'],
                   tow_data['v'], tow_data['o'])
tug_Resistance = f(tug_data['length'], tug_data['b'], tug_data['d'],
                   tug_data['v'], tug_data['o'])
print(f'被拖船的阻力是：{int(tow_Resistance)}Kn')  # f-string 不需要额外加引号。
print(f'拖轮的阻力是：{int(tug_Resistance)}Kn')
total_Resistance = tow_Resistance + tug_Resistance
a = int(total_Resistance / 9.8)
print(f"故此次拖带的总阻力为:{a}T")
