'''
扇形统计图工具类
'''
from pyecharts import Pie

class Rose():
    '''
    车牌类型统计
    '''

    def carTypeRose(self, data):
        attr = []
        v1 = []
        for row in data:
            licenseType = row[0]
            count = row[1]
            if licenseType == "0":
                licenseType = "标准民用车"
            elif licenseType == "4":
                licenseType = "使馆车牌"
            elif licenseType == "6":
                licenseType = "摩托车牌"
            elif licenseType == "8":
                licenseType = "运输车牌"
            attr.append(licenseType)
            v1.append(count)
        pie = Pie("24号车牌类型统计", width=1500, height=600, title_pos='center')
        pie.add("", attr, v1, label_text_color=None,
                is_label_show=True,
                legend_orient="vertical",
                legend_pos="left", )
        pie.render(path="./GUI/24号车牌类型统计.html")

    '''
    车辆在换电站所待时间信息统计
    '''

    def carInStationRose(self, data):
        attr = []
        v1 = []
        for row in data:
            second = row[0]
            count = row[1]
            attr.append(second)
            v1.append(count)
        pie = Pie("车辆在换电站所待时间信息统计", width=1500, height=600, title_pos='center')
        pie.add("", attr, v1, label_text_color=None,
                is_label_show=True,
                legend_orient="vertical",
                legend_pos="left", )
        pie.render(path="./GUI/24号车待的时间统计.html")


