
from pyecharts import Map,Geo

#世界地图数据
from economic.models import Area_gdp

value = [95.1,23.2,43.3,66.4,88.5]
attr = ['china','Canada','Brazil','Russia','United States']
# 省和直辖市
#从数据库中获取数据.
number = Area_gdp.objects.get(year=2015)
print(number.beijing)
province_distribution = {'河南':45.23,'北京': 37.56,
                         '河北': 21,'辽宁':12,'江西': 6,'上海':20,
                         '安徽':10,'江苏':16,'湖南':9,'浙江':13,
                         '海南':2,'广东':22,'湖北':8,'黑龙江':11,
                         '澳门':1,'陕西':11,'四川':7,'内蒙古':3,
                         '重庆':3,'云南':6,'贵州':2,'吉林':3,'山西':12,
                         '山东':11,'福建':4,'青海':1,'天津':1,'其他':1}
provice = list(province_distribution.keys())
values = list(province_distribution.values())

#城市,指定省的城市

city = ['郑州市','安阳市','洛阳市','濮阳市','南阳市','开封市','商丘市',
        '信阳市','新乡市']
values2 = [1.07,3.85,6.38,8.21,2.53,4.37,9.38,4.29,6.1]

#区县,具体城市内的区县
quxian = ['舞钢市','叶县','汝州市','宝丰县','鲁山县']
values3 = [3,5,7,8,2]


#中国地图
map = Map("2015中国经济占比地图",'2015中国经济占比地图', width=1200, height=600)
map.add("", provice, values, visual_range=[0, 50],  maptype='china', is_visualmap=True,
    visual_text_color='#000')
map.show_config()
# map.render(path="2015中国经济占比地图.html")























