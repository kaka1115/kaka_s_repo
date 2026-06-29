"在这里写实践，尝试用代码做点什么，这样学的才是最快的，正好可以用工作上的实践"

s = """《悦舟拖带成本报价》
1关于Day的参数：
Day1 是基地到起拖地的时间      D1
Day2 是起拖地到目的地的时间    D2
Day3 是目的地返回基地的时间    D3
DayPOL 是在起拖地港口的时间    DPOL
DayPOD 是在目的地港口的时间    DPOD
2关于速度的参数：
Speed1 是基地到起拖地的速度     S1
Speed2 是起拖地到目的地的速度    S2
Speed3 是目的地返回基地的速度    S3
3关于航线路程的参数：
Miles1 是基地到起拖地的海里      M1
Miles2 是起拖地到目的地的海里    M2
Miles3 是目的地返回基地的海里    M3
"""
"""
定义公式，就是用无形的线把各个元素连起来。
"""
data = {  #定义字典
    'L海':10,  # 海上每日耗油量 L海 LMGO1
    'L港':1,  # 港口每日耗油量  L港 LMGO2
    'PL':850,  # 当日油价   PL PRICE_LMGO
    'TCC':6500,  # 每日期租价格 每天多少钱 TCC TimeChartercost
    'S1':8,  # 第一段航行的速度Spped1
    'S2':5,  # 第二段航行的速度Speed2
    'S3':8,  # 第三段航行的速度Speed3
    'DPOL':2,  # 在起拖港的免费时间
    'DPOD':2,  # 在目的港的免费时间
    'M1':150,  # 第一段航行的公里数Miles1
    'M2':3272,  # 第二段航行的公里数Miles2
    'M3':3122  # 第三段航行的公里数Miles3
}

# 求航行天数
D1 = data['M1'] / data['S1'] / 24  # 第一段航行的天数Day1
D2 = data['M2'] /data['S2'] / 24  # 第二段航行的天数Day2
D3 = data['M3'] /data['S3'] / 24  # 第三段航行的天数Day3

# 求每段的耗油量，C就是Cost , 先路程的油耗成本。
C1 = C2 = C3 = D1 * data['L海'] * data['PL']

C4 = data['DPOL'] * data['L港'] * data['PL']
C5 = data['DPOD'] * data['L港'] * data['PL']

# 求总共用的天数，计算时间成本。
D = D1 + D2 + D3 + data['DPOL'] + data['DPOD']
C6 = D * data['TCC']

# 最后求总和成本
C7 = C1 + C2 + C3 + C4 + C5 + C6

print('本次拖带的总成本是', C7)
