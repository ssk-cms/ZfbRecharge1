'''
绘制折线图的工具类
'''
from pyecharts import Line

class LineChart():

    '''
    每半小时换电站内进入车辆信息统计
    '''
    def HalfHourLine(self,data):
        attr1 = []
        v1 = []
        total1 = 0
        for row in data:
            hour = row[0]
            minute = row[1]
            count = row[2]

            total1 += count

            attr1.append(hour + ":" + minute)
            v1.append(count)

        line = Line("24号每半小时换电站内进入车辆信息统计", "该日车辆总数为" + str(total1), width=1500, height=600)
        line.add("24号进入换电站车辆数量", attr1, v1, mark_line=["average"], mark_point=["max", "min"])
        line.render(path="./GUI/24号每隔半小时进入换电站车辆信息统计.html")

    '''
    全部数据分时间段换电站内进入车辆信息统计
    '''
    def StationLine(self,data):
        attr2 = []
        v2 = []
        total2 = 0
        for row in data:
            hour = row[0]
            minute = row[1]
            count = row[2]

            total2 += count
            if hour == None and minute == None:
                attr2.append("无时间")
            else:
                attr2.append(hour + ":" + minute)
            v2.append(count)

        line = Line("全部数据分时间段换电站内进入车辆信息统计", "车辆总数为" + str(total2), width=1500, height=600)
        line.add("全部数据分时间段进入换电站车辆数量", attr2, v2, mark_line=["max", "average", "min"])
        line.render(path="./GUI/全部数据每隔半小时进入换电站车辆信息统计.html")


