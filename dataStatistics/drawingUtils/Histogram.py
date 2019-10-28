'''
柱状图工具类
'''
from pyecharts import Bar


class Histogram():

    def driverStatus(self, data):
        value1 = []
        value2 = []
        value3 = []
        value4 = []
        hz = None
        wx = None
        gz = None
        sz = None
        # 设置行名
        columns = ["入职中司机", "在职司机", "离职司机", "异常司机"]
        # // 设置数据
        for i in data[0]:
            value1.append(int(i))
        value1.remove(value1[0])
        for d in data[1]:
            value2.append(int(d))
        value2.remove(value2[0])
        for d in data[2]:
            value3.append(int(d))
        value3.remove(value3[0])
        for d in data[3]:
            print(d)
            value4.append(int(d))
        value4.remove(value4[0])
        # 设置柱状图的主标题与副标题
        bar = Bar("司机状态统计")
        # // 添加柱状图的数据及配置项
        bar.add("杭州", columns, value1, mark_line=["average"], mark_point=["max", "min"])
        bar.add("无锡", columns, value2, mark_line=["average"], mark_point=["max", "min"])
        bar.add("广州", columns, value3, mark_line=["average"], mark_point=["max", "min"])
        bar.add("苏州", columns, value4, mark_line=["average"], mark_point=["max", "min"])
        # // 生成本地文件（默认为.html文件）
        bar.render(path="./GUI/司机状态.html")
