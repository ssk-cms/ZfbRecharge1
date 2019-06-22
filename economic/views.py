import os
import time

from django.http import HttpResponse

os.environ.update({"DJANGO_SETTINGS_MODULE": "cms.settings"})

from django.shortcuts import render
from pyecharts import Map, Geo, Bar3D, Funnel, Line, Polar, Pie

# 世界地图数据
from economic.models import Area_gdp, Gdp_compose, Gdp, Consum_level


# Create your views here.

def GDP_views(request):
    return render(request,'effectScatter-bmap.html')

#生成2015年全国经济地图的展示信息
def Number_2011(request):
    value = [95.1, 23.2, 43.3, 66.4, 88.5]
    attr = ['china', 'Canada', 'Brazil', 'Russia', 'United States']
    # 省和直辖市
    # 从数据库中获取数据.
    number = Area_gdp.objects.get(year=2011)
    province_distribution = {'河南': number.henan, '北京': number.beijing,
                             '河北': number.hebei, '辽宁': number.liaoning, '江西': number.jiangxi, '上海': number.shanghai,
                             '安徽': number.anhui, '江苏': number.jiangsu, '湖南': number.hunan, '浙江': number.zhejiang,
                             '海南': number.hainan, '广东': number.guangdong, '湖北': number.hubei, '黑龙江': number.heilongjiang,
                             '新疆': number.xinjiang, '陕西': number.shangxi, '四川': number.sichuan, '内蒙古': number.neimenggu,
                             '重庆': number.chongqing, '云南': number.yunnan, '贵州': number.guizhou, '吉林': number.jilin, '山西': number.shanxi,
                             '山东': number.shandong, '福建': number.fujian, '青海': number.qinghai, '天津': number.tianjin, '西藏': number.xizang,
                             '甘肃':number.gansu,'广西':number.guangxi,'宁夏':number.ningxia,'其他':''}
    provice = list(province_distribution.keys())
    values = list(province_distribution.values())

    # 城市,指定省的城市

    city = ['郑州市', '安阳市', '洛阳市', '濮阳市', '南阳市', '开封市', '商丘市',
            '信阳市', '新乡市']
    values2 = [1.07, 3.85, 6.38, 8.21, 2.53, 4.37, 9.38, 4.29, 6.1]

    # 区县,具体城市内的区县
    quxian = ['舞钢市', '叶县', '汝州市', '宝丰县', '鲁山县']
    values3 = [3, 5, 7, 8, 2]

    # 中国地图
    map = Map("2011中国经济占比地图", '单位:亿元', width=1200, height=600)
    map.add("", provice, values, visual_range=[0, 100000], maptype='china', is_visualmap=True,
            visual_text_color='#000')
    map.show_config()
    map.render(path="F:/尚世康资料/尚世康+毕业论文相关资料/系统设计/cms/templates/2011中国经济占比地图.html")
    return HttpResponse('生成成功')

def Number_2012(request):
    value = [95.1, 23.2, 43.3, 66.4, 88.5]
    attr = ['china', 'Canada', 'Brazil', 'Russia', 'United States']
    # 省和直辖市
    # 从数据库中获取数据.
    number = Area_gdp.objects.get(year=2012)
    province_distribution = {'河南': number.henan, '北京': number.beijing,
                             '河北': number.hebei, '辽宁': number.liaoning, '江西': number.jiangxi, '上海': number.shanghai,
                             '安徽': number.anhui, '江苏': number.jiangsu, '湖南': number.hunan, '浙江': number.zhejiang,
                             '海南': number.hainan, '广东': number.guangdong, '湖北': number.hubei, '黑龙江': number.heilongjiang,
                             '新疆': number.xinjiang, '陕西': number.shangxi, '四川': number.sichuan, '内蒙古': number.neimenggu,
                             '重庆': number.chongqing, '云南': number.yunnan, '贵州': number.guizhou, '吉林': number.jilin, '山西': number.shanxi,
                             '山东': number.shandong, '福建': number.fujian, '青海': number.qinghai, '天津': number.tianjin, '西藏': number.xizang,
                             '甘肃':number.gansu,'广西':number.guangxi,'其他':'','宁夏':number.ningxia}
    provice = list(province_distribution.keys())
    values = list(province_distribution.values())

    # 城市,指定省的城市

    city = ['郑州市', '安阳市', '洛阳市', '濮阳市', '南阳市', '开封市', '商丘市',
            '信阳市', '新乡市']
    values2 = [1.07, 3.85, 6.38, 8.21, 2.53, 4.37, 9.38, 4.29, 6.1]

    # 区县,具体城市内的区县
    quxian = ['舞钢市', '叶县', '汝州市', '宝丰县', '鲁山县']
    values3 = [3, 5, 7, 8, 2]

    # 中国地图
    map = Map("2012中国经济占比地图", '单位:亿元', width=1200, height=600)
    map.add("", provice, values, visual_range=[0, 100000], maptype='china', is_visualmap=True,
            visual_text_color='#000')
    map.show_config()
    map.render(path="F:/尚世康资料/尚世康+毕业论文相关资料/系统设计/cms/templates/2012中国经济占比地图.html")
    return HttpResponse('生成成功')

def Number_2013(request):
    value = [95.1, 23.2, 43.3, 66.4, 88.5]
    attr = ['china', 'Canada', 'Brazil', 'Russia', 'United States']
    # 省和直辖市
    # 从数据库中获取数据.
    number = Area_gdp.objects.get(year=2013)
    province_distribution = {'河南': number.henan, '北京': number.beijing,
                             '河北': number.hebei, '辽宁': number.liaoning, '江西': number.jiangxi, '上海': number.shanghai,
                             '安徽': number.anhui, '江苏': number.jiangsu, '湖南': number.hunan, '浙江': number.zhejiang,
                             '海南': number.hainan, '广东': number.guangdong, '湖北': number.hubei, '黑龙江': number.heilongjiang,
                             '新疆': number.xinjiang, '陕西': number.shangxi, '四川': number.sichuan, '内蒙古': number.neimenggu,
                             '重庆': number.chongqing, '云南': number.yunnan, '贵州': number.guizhou, '吉林': number.jilin, '山西': number.shanxi,
                             '山东': number.shandong, '福建': number.fujian, '青海': number.qinghai, '天津': number.tianjin, '西藏': number.xizang,
                             '甘肃':number.gansu,'广西':number.guangxi,'其他':'','宁夏':number.ningxia}
    provice = list(province_distribution.keys())
    values = list(province_distribution.values())

    # 城市,指定省的城市

    city = ['郑州市', '安阳市', '洛阳市', '濮阳市', '南阳市', '开封市', '商丘市',
            '信阳市', '新乡市']
    values2 = [1.07, 3.85, 6.38, 8.21, 2.53, 4.37, 9.38, 4.29, 6.1]

    # 区县,具体城市内的区县
    quxian = ['舞钢市', '叶县', '汝州市', '宝丰县', '鲁山县']
    values3 = [3, 5, 7, 8, 2]

    # 中国地图
    map = Map("2013中国经济占比地图", '单位:亿元', width=1200, height=600)
    map.add("", provice, values, visual_range=[0, 100000], maptype='china', is_visualmap=True,
            visual_text_color='#000')
    map.show_config()
    map.render(path="F:/尚世康资料/尚世康+毕业论文相关资料/系统设计/cms/templates/2013中国经济占比地图.html")
    return HttpResponse('生成成功')

def Number_2014(request):
    value = [95.1, 23.2, 43.3, 66.4, 88.5]
    attr = ['china', 'Canada', 'Brazil', 'Russia', 'United States']
    # 省和直辖市
    # 从数据库中获取数据.
    number = Area_gdp.objects.get(year=2014)
    province_distribution = {'河南': number.henan, '北京': number.beijing,
                             '河北': number.hebei, '辽宁': number.liaoning, '江西': number.jiangxi, '上海': number.shanghai,
                             '安徽': number.anhui, '江苏': number.jiangsu, '湖南': number.hunan, '浙江': number.zhejiang,
                             '海南': number.hainan, '广东': number.guangdong, '湖北': number.hubei, '黑龙江': number.heilongjiang,
                             '新疆': number.xinjiang, '陕西': number.shangxi, '四川': number.sichuan, '内蒙古': number.neimenggu,
                             '重庆': number.chongqing, '云南': number.yunnan, '贵州': number.guizhou, '吉林': number.jilin, '山西': number.shanxi,
                             '山东': number.shandong, '福建': number.fujian, '青海': number.qinghai, '天津': number.tianjin, '西藏': number.xizang,
                             '甘肃':number.gansu,'广西':number.guangxi,'其他':'','宁夏':number.ningxia}
    provice = list(province_distribution.keys())
    values = list(province_distribution.values())

    # 城市,指定省的城市

    city = ['郑州市', '安阳市', '洛阳市', '濮阳市', '南阳市', '开封市', '商丘市',
            '信阳市', '新乡市']
    values2 = [1.07, 3.85, 6.38, 8.21, 2.53, 4.37, 9.38, 4.29, 6.1]

    # 区县,具体城市内的区县
    quxian = ['舞钢市', '叶县', '汝州市', '宝丰县', '鲁山县']
    values3 = [3, 5, 7, 8, 2]

    # 中国地图
    map = Map("2014中国经济占比地图", '单位:亿元', width=1200, height=600)
    map.add("", provice, values, visual_range=[0, 100000], maptype='china', is_visualmap=True,
            visual_text_color='#000')
    map.show_config()
    map.render(path="F:/尚世康资料/尚世康+毕业论文相关资料/系统设计/cms/templates/2014中国经济占比地图.html")
    return HttpResponse('生成成功')

def Number_2015(request):
    value = [95.1, 23.2, 43.3, 66.4, 88.5]
    attr = ['china', 'Canada', 'Brazil', 'Russia', 'United States']
    # 省和直辖市
    # 从数据库中获取数据.
    number = Area_gdp.objects.get(year=2015)
    province_distribution = {'河南': number.henan, '北京': number.beijing,
                             '河北': number.hebei, '辽宁': number.liaoning, '江西': number.jiangxi, '上海': number.shanghai,
                             '安徽': number.anhui, '江苏': number.jiangsu, '湖南': number.hunan, '浙江': number.zhejiang,
                             '海南': number.hainan, '广东': number.guangdong, '湖北': number.hubei, '黑龙江': number.heilongjiang,
                             '新疆': number.xinjiang, '陕西': number.shangxi, '四川': number.sichuan, '内蒙古': number.neimenggu,
                             '重庆': number.chongqing, '云南': number.yunnan, '贵州': number.guizhou, '吉林': number.jilin, '山西': number.shanxi,
                             '山东': number.shandong, '福建': number.fujian, '青海': number.qinghai, '天津': number.tianjin, '西藏': number.xizang,
                             '甘肃':number.gansu,'广西':number.guangxi,'其他':'','宁夏':number.ningxia}
    provice = list(province_distribution.keys())
    values = list(province_distribution.values())

    # 城市,指定省的城市

    city = ['郑州市', '安阳市', '洛阳市', '濮阳市', '南阳市', '开封市', '商丘市',
            '信阳市', '新乡市']
    values2 = [1.07, 3.85, 6.38, 8.21, 2.53, 4.37, 9.38, 4.29, 6.1]

    # 区县,具体城市内的区县
    quxian = ['舞钢市', '叶县', '汝州市', '宝丰县', '鲁山县']
    values3 = [3, 5, 7, 8, 2]

    # 中国地图
    map = Map("2015中国经济占比地图", '单位:亿元', width=1200, height=600)
    map.add("", provice, values, visual_range=[0, 100000], maptype='china', is_visualmap=True,
            visual_text_color='#000')
    map.show_config()
    map.render(path="F:/尚世康资料/尚世康+毕业论文相关资料/系统设计/cms/templates/2015中国经济占比地图.html")
    return HttpResponse('生成成功')


def Number_2016(request):
    value = [95.1, 23.2, 43.3, 66.4, 88.5]
    attr = ['china', 'Canada', 'Brazil', 'Russia', 'United States']
    # 省和直辖市
    # 从数据库中获取数据.
    number = Area_gdp.objects.get(year=2016)
    province_distribution = {'河南': number.henan, '北京': number.beijing,
                             '河北': number.hebei, '辽宁': number.liaoning, '江西': number.jiangxi, '上海': number.shanghai,
                             '安徽': number.anhui, '江苏': number.jiangsu, '湖南': number.hunan, '浙江': number.zhejiang,
                             '海南': number.hainan, '广东': number.guangdong, '湖北': number.hubei, '黑龙江': number.heilongjiang,
                             '新疆': number.xinjiang, '陕西': number.shangxi, '四川': number.sichuan, '内蒙古': number.neimenggu,
                             '重庆': number.chongqing, '云南': number.yunnan, '贵州': number.guizhou, '吉林': number.jilin, '山西': number.shanxi,
                             '山东': number.shandong, '福建': number.fujian, '青海': number.qinghai, '天津': number.tianjin, '西藏': number.xizang,
                             '甘肃':number.gansu,'广西':number.guangxi,'其他':'','宁夏':number.ningxia}
    provice = list(province_distribution.keys())
    values = list(province_distribution.values())

    # 城市,指定省的城市

    city = ['郑州市', '安阳市', '洛阳市', '濮阳市', '南阳市', '开封市', '商丘市',
            '信阳市', '新乡市']
    values2 = [1.07, 3.85, 6.38, 8.21, 2.53, 4.37, 9.38, 4.29, 6.1]

    # 区县,具体城市内的区县
    quxian = ['舞钢市', '叶县', '汝州市', '宝丰县', '鲁山县']
    values3 = [3, 5, 7, 8, 2]

    # 中国地图
    map = Map("2016中国经济占比地图", '单位:亿元', width=1200, height=600)
    map.add("", provice, values, visual_range=[0, 100000], maptype='china', is_visualmap=True,
            visual_text_color='#000')
    map.show_config()
    map.render(path="F:/尚世康资料/尚世康+毕业论文相关资料/系统设计/cms/templates/2016中国经济占比地图.html")
    return HttpResponse('生成成功')

def Number_2017(request):
    value = [95.1, 23.2, 43.3, 66.4, 88.5]
    attr = ['china', 'Canada', 'Brazil', 'Russia', 'United States']
    # 省和直辖市
    # 从数据库中获取数据.
    number = Area_gdp.objects.get(year=2017)
    province_distribution = {'河南': number.henan, '北京': number.beijing,
                             '河北': number.hebei, '辽宁': number.liaoning, '江西': number.jiangxi, '上海': number.shanghai,
                             '安徽': number.anhui, '江苏': number.jiangsu, '湖南': number.hunan, '浙江': number.zhejiang,
                             '海南': number.hainan, '广东': number.guangdong, '湖北': number.hubei, '黑龙江': number.heilongjiang,
                             '新疆': number.xinjiang, '陕西': number.shangxi, '四川': number.sichuan, '内蒙古': number.neimenggu,
                             '重庆': number.chongqing, '云南': number.yunnan, '贵州': number.guizhou, '吉林': number.jilin, '山西': number.shanxi,
                             '山东': number.shandong, '福建': number.fujian, '青海': number.qinghai, '天津': number.tianjin, '西藏': number.xizang,
                             '甘肃':number.gansu,'广西':number.guangxi,'其他':'','宁夏':number.ningxia}
    provice = list(province_distribution.keys())
    values = list(province_distribution.values())

    # 城市,指定省的城市

    city = ['郑州市', '安阳市', '洛阳市', '濮阳市', '南阳市', '开封市', '商丘市',
            '信阳市', '新乡市']
    values2 = [1.07, 3.85, 6.38, 8.21, 2.53, 4.37, 9.38, 4.29, 6.1]

    # 区县,具体城市内的区县
    quxian = ['舞钢市', '叶县', '汝州市', '宝丰县', '鲁山县']
    values3 = [3, 5, 7, 8, 2]

    # 中国地图
    map = Map("2017中国经济占比地图", '单位:亿元', width=1200, height=600)
    map.add("", provice, values, visual_range=[0, 100000], maptype='china', is_visualmap=True,
            visual_text_color='#000')
    map.show_config()
    map.render(path="F:/尚世康资料/尚世康+毕业论文相关资料/系统设计/cms/templates/2017中国经济占比地图.html")
    return HttpResponse('生成成功')


def Zhuzhaungtu3d(request):
    bar3d = Bar3D("3D 地区经济对比", width=1500, height=800)
    y_axis= [
        "北京", "天津", "河北", "山西", "内蒙古", "辽宁", "吉林", "黑龙江", "上海", "江苏", "浙江", "安徽",
        "福建", "江西", "山东", "河南", "湖北", "湖南", "广东", "广西", "海南", "重庆", "四川", "贵州","云南",
        "西藏","陕西","甘肃","青海","宁夏","新疆"
    ]
    x_axis = [
        "2011年", "2012年", "2013年", "2014年", "2015年", "2016年", "2017年"
    ]

    number_2011 = Area_gdp.objects.get(year=2011)
    number_2012 = Area_gdp.objects.get(year=2012)
    number_2013 = Area_gdp.objects.get(year=2013)
    number_2014 = Area_gdp.objects.get(year=2014)
    number_2015 = Area_gdp.objects.get(year=2015)
    number_2016 = Area_gdp.objects.get(year=2016)
    number_2017 = Area_gdp.objects.get(year=2017)
    data = [
        [ 0,0, number_2011.beijing], [1, 0, number_2011.tianjin], [2, 0, number_2011.hebei], [3, 0, number_2011.shanxi], [4, 0, number_2011.neimenggu], [5, 0, number_2011.liaoning],
        [6, 0, number_2011.jilin], [7, 0, number_2011.heilongjiang], [8, 0, number_2011.shanghai], [9, 0, number_2011.jiangsu], [10, 0, number_2011.zhejiang], [11, 0, number_2011.anhui],
        [12, 0, number_2011.fujian], [13, 0, number_2011.jiangxi], [14, 0, number_2011.shandong], [15, 0, number_2011.henan], [16, 0, number_2011.hubei], [17, 0, number_2011.hunan],
        [18, 0, number_2011.guangdong], [19, 0, number_2011.guangxi], [20, 0, number_2011.hainan], [21, 0, number_2011.chongqing], [22, 0, number_2011.sichuan], [23, 0, number_2011.guizhou],
        [24,0,number_2011.yunnan],[25,0,number_2011.xizang],[26,0,number_2011.shangxi],[27,0,number_2011.gansu],[28,0,number_2011.qinghai],[29,0,number_2011.ningxia],[30,0,number_2011.xinjiang],

        [0, 1, number_2012.beijing], [1, 1, number_2012.tianjin], [2, 1, number_2012.hebei], [3, 1, number_2012.shanxi], [4, 1, number_2012.neimenggu], [5, 1, number_2012.liaoning],
        [6, 1, number_2012.jilin], [7, 1, number_2012.heilongjiang], [8, 1, number_2012.shanghai], [9, 1, number_2012.jiangsu], [10, 1, number_2012.zhejiang], [11, 1, number_2012.anhui],
        [12, 1, number_2012.fujian], [13, 1, number_2012.jiangxi], [14, 1, number_2012.shandong], [15, 1, number_2012.henan], [16, 1, number_2012.hubei], [17, 1, number_2012.hunan],
        [18, 1, number_2012.guangdong], [19, 1, number_2012.guangxi], [20, 1, number_2012.hainan], [21, 1, number_2012.chongqing], [22, 1, number_2012.sichuan], [23, 1, number_2012.guizhou],
        [24,1,number_2012.yunnan],[25,1,number_2012.xizang],[26,1,number_2012.shangxi],[27,1,number_2012.gansu],[28,1,number_2012.qinghai],[29,1,number_2012.ningxia],[30,1,number_2012.xinjiang],

        [0, 2, number_2013.beijing], [1, 2, number_2013.tianjin], [2, 2, number_2013.hebei], [3, 2, number_2013.shanxi],
        [4, 2, number_2013.neimenggu], [5, 2, number_2013.liaoning],
        [6, 2, number_2013.jilin], [7, 2, number_2013.heilongjiang], [8, 2, number_2013.shanghai],
        [9, 2, number_2013.jiangsu], [10, 2, number_2013.zhejiang], [11, 2, number_2013.anhui],
        [12, 2, number_2013.fujian], [13, 2, number_2013.jiangxi], [14, 2, number_2013.shandong],
        [15, 2, number_2013.henan], [16, 2, number_2013.hubei], [17, 2, number_2013.hunan],
        [18, 2, number_2013.guangdong], [19, 2, number_2013.guangxi], [20, 2, number_2013.hainan],
        [21, 2, number_2013.chongqing], [22, 2, number_2013.sichuan], [23, 2, number_2013.guizhou],
        [24, 2, number_2013.yunnan], [25, 2, number_2013.xizang], [26, 2, number_2013.shangxi],
        [27, 2, number_2013.gansu], [28, 2, number_2013.qinghai], [29, 2, number_2013.ningxia],
        [30, 2, number_2013.xinjiang],

        [0, 3, number_2014.beijing], [1, 3, number_2014.tianjin], [2, 3, number_2014.hebei], [3, 3, number_2014.shanxi],
        [4, 3, number_2014.neimenggu], [5, 3, number_2014.liaoning],
        [6, 3, number_2014.jilin], [7, 3, number_2014.heilongjiang], [8, 3, number_2014.shanghai],
        [9, 3, number_2014.jiangsu], [10, 3, number_2014.zhejiang], [11, 3, number_2014.anhui],
        [12, 3, number_2014.fujian], [13, 3, number_2014.jiangxi], [14, 3, number_2014.shandong],
        [15, 3, number_2014.henan], [16, 3, number_2014.hubei], [17, 3, number_2014.hunan],
        [18, 3, number_2014.guangdong], [19, 3, number_2014.guangxi], [20, 3, number_2014.hainan],
        [21, 3, number_2014.chongqing], [22, 3, number_2014.sichuan], [23, 3, number_2014.guizhou],
        [24, 3, number_2014.yunnan], [25, 3, number_2014.xizang], [26, 3, number_2014.shangxi],
        [27, 3, number_2014.gansu], [28, 3, number_2014.qinghai], [29, 3, number_2014.ningxia],
        [30, 3, number_2014.xinjiang],

        [0, 4, number_2015.beijing], [1, 4, number_2015.tianjin], [2, 4, number_2015.hebei], [3, 4, number_2015.shanxi],
        [4, 4, number_2015.neimenggu], [5, 4, number_2015.liaoning],
        [6, 4, number_2015.jilin], [7, 4, number_2015.heilongjiang], [8, 4, number_2015.shanghai],
        [9, 4, number_2015.jiangsu], [10, 4, number_2015.zhejiang], [11, 4, number_2015.anhui],
        [12, 4, number_2015.fujian], [13, 4, number_2015.jiangxi], [14, 4, number_2015.shandong],
        [15, 4, number_2015.henan], [16, 4, number_2015.hubei], [17, 4, number_2015.hunan],
        [18, 4, number_2015.guangdong], [19, 4, number_2015.guangxi], [20, 4, number_2015.hainan],
        [21, 4, number_2015.chongqing], [22, 4, number_2015.sichuan], [23, 4, number_2015.guizhou],
        [24, 4, number_2015.yunnan], [25, 4, number_2015.xizang], [26, 4, number_2015.shangxi],
        [27, 4, number_2015.gansu], [28, 4, number_2015.qinghai], [29, 4, number_2015.ningxia],
        [30, 4, number_2015.xinjiang],

        [0, 5, number_2016.beijing], [1, 5, number_2016.tianjin], [2, 5, number_2016.hebei], [5, 3, number_2016.shanxi],
        [4, 5, number_2016.neimenggu], [5, 5, number_2016.liaoning],
        [6, 5, number_2016.jilin], [7, 5, number_2016.heilongjiang], [8, 5, number_2016.shanghai],
        [9, 5, number_2016.jiangsu], [10, 5, number_2016.zhejiang], [11, 5, number_2016.anhui],
        [12, 5, number_2016.fujian], [13, 5, number_2016.jiangxi], [14, 5, number_2016.shandong],
        [15, 5, number_2016.henan], [16, 5, number_2016.hubei], [17, 5, number_2016.hunan],
        [18, 5, number_2016.guangdong], [19, 5, number_2016.guangxi], [20, 5, number_2016.hainan],
        [21, 5, number_2016.chongqing], [22, 5, number_2016.sichuan], [23, 5, number_2016.guizhou],
        [24, 5, number_2016.yunnan], [25, 5, number_2016.xizang], [26, 5, number_2016.shangxi],
        [27, 5, number_2016.gansu], [28, 5, number_2016.qinghai], [29, 5, number_2016.ningxia],
        [30, 5, number_2016.xinjiang],

        [0, 6, number_2017.beijing], [1, 6, number_2017.tianjin], [2, 6, number_2017.hebei], [3, 6, number_2017.shanxi],
        [4, 6, number_2017.neimenggu], [5, 6, number_2017.liaoning],
        [6, 6, number_2017.jilin], [7, 6, number_2017.heilongjiang], [8, 6, number_2017.shanghai],
        [9, 6, number_2017.jiangsu], [10, 6, number_2017.zhejiang], [11, 6, number_2017.anhui],
        [12, 6, number_2017.fujian], [13, 6, number_2017.jiangxi], [14, 6, number_2017.shandong],
        [15, 6, number_2017.henan], [16, 6, number_2017.hubei], [17, 6, number_2017.hunan],
        [18, 6, number_2017.guangdong], [19, 6, number_2017.guangxi], [20, 6, number_2017.hainan],
        [21, 6, number_2017.chongqing], [22, 6, number_2017.sichuan], [23, 6, number_2017.guizhou],
        [24, 6, number_2017.yunnan], [25, 6, number_2017.xizang], [26, 6, number_2017.shangxi],
        [27, 6, number_2017.gansu], [28, 6, number_2017.qinghai], [29, 6, number_2017.ningxia],
        [30, 6, number_2017.xinjiang]
    ]
    range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
                   '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    bar3d.add(
        "",
        x_axis,
        y_axis,
        [[d[1], d[0], d[2]] for d in data],
        is_visualmap=True,
        visual_range=[0, 100000],
        visual_range_color=range_color,
        grid3d_width=200,
        grid3d_depth=80,
        grid3d_shading="lambert",
        is_grid3d_rotate=True,
    )
    bar3d.render(path="F:/尚世康资料/尚世康+毕业论文相关资料/系统设计/cms/templates/地区GDP对比柱状图.html")
    return HttpResponse("3d柱状图已生成")


#地区经济漏斗图
def LouDou_2011(request):
    number = Area_gdp.objects.get(year=2011)
    attr = ["北京", "天津", "河北", "山西", "内蒙古", "辽宁",
            "吉林","黑龙江","上海","江苏","浙江","安徽","福建",
            "江西","山东","河南","湖北","湖南","广东","广西",
            "海南","重庆","四川","贵州","云南","西藏","陕西","甘肃",
            "青海","宁夏","新疆"]
    value = [number.beijing, number.tianjin, number.hebei, number.shanxi, number.neimenggu, number.liaoning,
             number.jilin,number.heilongjiang,number.shanghai,number.jiangsu,number.zhejiang,number.anhui,number.fujian,
             number.jiangxi,number.shandong,number.henan,number.hubei,number.hunan,number.guangdong,number.guangxi,
             number.hainan,number.chongqing,number.sichuan,number.guizhou,number.yunnan,number.xizang,number.shanxi,
             number.gansu,number.qinghai,number.ningxia,number.xinjiang]
    funnel = Funnel("2011年地区经济数据分析", width=1500, height=600, title_pos='center')
    funnel.add(
        "GDP",
        attr,
        value,
        is_label_show=True,
        label_pos="outside",
        label_text_color="#fff",
        funnel_sort="ascending",
        # funnel_gap=5,
        legend_orient="vertical",
        legend_pos="left",
    )
    funnel.render(path="F:/尚世康资料/尚世康+毕业论文相关资料/系统设计/cms/templates/2011年地区经济桶状图.html")

    return HttpResponse("2011年桶装图已生成")

def LouDou_2012(request):
    number = Area_gdp.objects.get(year=2012)
    attr = ["北京", "天津", "河北", "山西", "内蒙古", "辽宁",
            "吉林","黑龙江","上海","江苏","浙江","安徽","福建",
            "江西","山东","河南","湖北","湖南","广东","广西",
            "海南","重庆","四川","贵州","云南","西藏","陕西","甘肃",
            "青海","宁夏","新疆"]
    value = [number.beijing, number.tianjin, number.hebei, number.shanxi, number.neimenggu, number.liaoning,
             number.jilin,number.heilongjiang,number.shanghai,number.jiangsu,number.zhejiang,number.anhui,number.fujian,
             number.jiangxi,number.shandong,number.henan,number.hubei,number.hunan,number.guangdong,number.guangxi,
             number.hainan,number.chongqing,number.sichuan,number.guizhou,number.yunnan,number.xizang,number.shanxi,
             number.gansu,number.qinghai,number.ningxia,number.xinjiang]
    funnel = Funnel("2012年地区经济数据分析", width=1500, height=600, title_pos='center')
    funnel.add(
        "GDP",
        attr,
        value,
        is_label_show=True,
        label_pos="outside",
        label_text_color="#fff",
        funnel_sort="ascending",
        # funnel_gap=5,
        legend_orient="vertical",
        legend_pos="left",
    )
    funnel.render(path="F:/尚世康资料/尚世康+毕业论文相关资料/系统设计/cms/templates/2012年地区经济桶状图.html")

    return HttpResponse("2012年桶装图已生成")

def LouDou_2013(request):
    number = Area_gdp.objects.get(year=2013)
    attr = ["北京", "天津", "河北", "山西", "内蒙古", "辽宁",
            "吉林","黑龙江","上海","江苏","浙江","安徽","福建",
            "江西","山东","河南","湖北","湖南","广东","广西",
            "海南","重庆","四川","贵州","云南","西藏","陕西","甘肃",
            "青海","宁夏","新疆"]
    value = [number.beijing, number.tianjin, number.hebei, number.shanxi, number.neimenggu, number.liaoning,
             number.jilin,number.heilongjiang,number.shanghai,number.jiangsu,number.zhejiang,number.anhui,number.fujian,
             number.jiangxi,number.shandong,number.henan,number.hubei,number.hunan,number.guangdong,number.guangxi,
             number.hainan,number.chongqing,number.sichuan,number.guizhou,number.yunnan,number.xizang,number.shanxi,
             number.gansu,number.qinghai,number.ningxia,number.xinjiang]
    funnel = Funnel("2013年地区经济数据分析", width=1500, height=600, title_pos='center')
    funnel.add(
        "GDP",
        attr,
        value,
        is_label_show=True,
        label_pos="outside",
        label_text_color="#fff",
        funnel_sort="ascending",
        # funnel_gap=5,
        legend_orient="vertical",
        legend_pos="left",
    )
    funnel.render(path="F:/尚世康资料/尚世康+毕业论文相关资料/系统设计/cms/templates/2013年地区经济桶状图.html")

    return HttpResponse("2013年桶装图已生成")

def LouDou_2014(request):
    number = Area_gdp.objects.get(year=2014)
    attr = ["北京", "天津", "河北", "山西", "内蒙古", "辽宁",
            "吉林","黑龙江","上海","江苏","浙江","安徽","福建",
            "江西","山东","河南","湖北","湖南","广东","广西",
            "海南","重庆","四川","贵州","云南","西藏","陕西","甘肃",
            "青海","宁夏","新疆"]
    value = [number.beijing, number.tianjin, number.hebei, number.shanxi, number.neimenggu, number.liaoning,
             number.jilin,number.heilongjiang,number.shanghai,number.jiangsu,number.zhejiang,number.anhui,number.fujian,
             number.jiangxi,number.shandong,number.henan,number.hubei,number.hunan,number.guangdong,number.guangxi,
             number.hainan,number.chongqing,number.sichuan,number.guizhou,number.yunnan,number.xizang,number.shanxi,
             number.gansu,number.qinghai,number.ningxia,number.xinjiang]
    funnel = Funnel("2014年地区经济数据分析", width=1500, height=600, title_pos='center')
    funnel.add(
        "GDP",
        attr,
        value,
        is_label_show=True,
        label_pos="outside",
        label_text_color="#fff",
        funnel_sort="ascending",
        # funnel_gap=5,
        legend_orient="vertical",
        legend_pos="left",
    )
    funnel.render(path="F:/尚世康资料/尚世康+毕业论文相关资料/系统设计/cms/templates/2014年地区经济桶状图.html")

    return HttpResponse("2014年桶装图已生成")

def LouDou_2015(request):
    number = Area_gdp.objects.get(year=2015)
    attr = ["北京", "天津", "河北", "山西", "内蒙古", "辽宁",
            "吉林","黑龙江","上海","江苏","浙江","安徽","福建",
            "江西","山东","河南","湖北","湖南","广东","广西",
            "海南","重庆","四川","贵州","云南","西藏","陕西","甘肃",
            "青海","宁夏","新疆"]
    value = [number.beijing, number.tianjin, number.hebei, number.shanxi, number.neimenggu, number.liaoning,
             number.jilin,number.heilongjiang,number.shanghai,number.jiangsu,number.zhejiang,number.anhui,number.fujian,
             number.jiangxi,number.shandong,number.henan,number.hubei,number.hunan,number.guangdong,number.guangxi,
             number.hainan,number.chongqing,number.sichuan,number.guizhou,number.yunnan,number.xizang,number.shanxi,
             number.gansu,number.qinghai,number.ningxia,number.xinjiang]
    funnel = Funnel("2015年地区经济数据分析", width=1500, height=600, title_pos='center')
    funnel.add(
        "GDP",
        attr,
        value,
        is_label_show=True,
        label_pos="outside",
        label_text_color="#fff",
        funnel_sort="ascending",
        # funnel_gap=5,
        legend_orient="vertical",
        legend_pos="left",
    )
    funnel.render(path="F:/尚世康资料/尚世康+毕业论文相关资料/系统设计/cms/templates/2015年地区经济桶状图.html")

    return HttpResponse("2015年桶装图已生成")

def LouDou_2016(request):
    number = Area_gdp.objects.get(year=2016)
    attr = ["北京", "天津", "河北", "山西", "内蒙古", "辽宁",
            "吉林","黑龙江","上海","江苏","浙江","安徽","福建",
            "江西","山东","河南","湖北","湖南","广东","广西",
            "海南","重庆","四川","贵州","云南","西藏","陕西","甘肃",
            "青海","宁夏","新疆"]
    value = [number.beijing, number.tianjin, number.hebei, number.shanxi, number.neimenggu, number.liaoning,
             number.jilin,number.heilongjiang,number.shanghai,number.jiangsu,number.zhejiang,number.anhui,number.fujian,
             number.jiangxi,number.shandong,number.henan,number.hubei,number.hunan,number.guangdong,number.guangxi,
             number.hainan,number.chongqing,number.sichuan,number.guizhou,number.yunnan,number.xizang,number.shanxi,
             number.gansu,number.qinghai,number.ningxia,number.xinjiang]
    funnel = Funnel("2016年地区经济数据分析", width=1500, height=600, title_pos='center')
    funnel.add(
        "GDP",
        attr,
        value,
        is_label_show=True,
        label_pos="outside",
        label_text_color="#fff",
        funnel_sort="ascending",
        # funnel_gap=5,
        legend_orient="vertical",
        legend_pos="left",
    )
    funnel.render(path="F:/尚世康资料/尚世康+毕业论文相关资料/系统设计/cms/templates/2016年地区经济桶状图.html")

    return HttpResponse("2016年桶装图已生成")


def LouDou_2017(request):
    number = Area_gdp.objects.get(year=2017)
    attr = ["北京", "天津", "河北", "山西", "内蒙古", "辽宁",
            "吉林","黑龙江","上海","江苏","浙江","安徽","福建",
            "江西","山东","河南","湖北","湖南","广东","广西",
            "海南","重庆","四川","贵州","云南","西藏","陕西","甘肃",
            "青海","宁夏","新疆"]
    value = [number.beijing, number.tianjin, number.hebei, number.shanxi, number.neimenggu, number.liaoning,
             number.jilin,number.heilongjiang,number.shanghai,number.jiangsu,number.zhejiang,number.anhui,number.fujian,
             number.jiangxi,number.shandong,number.henan,number.hubei,number.hunan,number.guangdong,number.guangxi,
             number.hainan,number.chongqing,number.sichuan,number.guizhou,number.yunnan,number.xizang,number.shanxi,
             number.gansu,number.qinghai,number.ningxia,number.xinjiang]
    funnel = Funnel("2017年地区经济数据分析", width=1500, height=600, title_pos='center')
    funnel.add(
        "GDP",
        attr,
        value,
        is_label_show=True,
        label_pos="outside",
        label_text_color="#fff",
        funnel_sort="ascending",
        # funnel_gap=5,
        legend_orient="vertical",
        legend_pos="left",
    )
    funnel.render(path="F:/尚世康资料/尚世康+毕业论文相关资料/系统设计/cms/templates/2017年地区经济桶状图.html")

    return HttpResponse("2017年桶装图已生成")

#生产总值构成折线图
def Zhexiantu(request):

    attr = ["国民总收入","国内生产总值", "第一产业", "第二产业", "第三产业", "农林牧渔业",
            "工业","建筑业","批发和零售业","交通运输,仓储和邮政业",
            "住宿和餐饮业","金融业","房地产业","其他","人均国内生产总值(元)"]
    message_2015 = Gdp.objects.get(year=2015)
    message_2016 = Gdp.objects.get(year=2016)
    message_2017 = Gdp.objects.get(year=2017)
    v1 = [message_2015.gdp,message_2015.gross,message_2015.first_produce,message_2015.second_produce,message_2015.third_produce,
          message_2015.nong_lin_yu_muye,message_2015.industry,message_2015.construstion,message_2015.pifa_lingshouye,
          message_2015.traffic,message_2015.stay,message_2015.banking,message_2015.estate,message_2015.other,message_2015.ave_gdp]

    v2 = [message_2016.gdp, message_2016.gross,message_2016.first_produce, message_2016.second_produce, message_2016.third_produce,
          message_2016.nong_lin_yu_muye, message_2016.industry, message_2016.construstion, message_2016.pifa_lingshouye,
          message_2016.traffic, message_2016.stay, message_2016.banking, message_2016.estate, message_2016.other,message_2016.ave_gdp]

    v3 = [message_2017.gdp, message_2017.gross,message_2017.first_produce, message_2017.second_produce, message_2017.third_produce,
          message_2017.nong_lin_yu_muye, message_2017.industry, message_2017.construstion, message_2017.pifa_lingshouye,
          message_2017.traffic, message_2017.stay, message_2017.banking, message_2017.estate, message_2017.other,message_2017.ave_gdp]
    line = Line("GDP构成及分布图","单位(亿元)",width=1500,height=600)
    line.add("2015年", attr, v1, mark_point=["average"])
    line.add("2016年", attr, v2, is_smooth=True, mark_line=["max", "average"])
    line.add("2017年", attr, v3, is_smooth=True, mark_line=["max", "average"])
    line.render(path="F:/尚世康资料/尚世康+毕业论文相关资料/系统设计/cms/templates/GDP分布及构成图.html")

    return HttpResponse("GDP分布及构成图生成成功")


#各年份城乡居民消费水平对比
def Year_level(request):

    consume_level2011 = Consum_level.objects.get(id=17)
    consume_level2012 = Consum_level.objects.get(id=18)
    consume_level2013 = Consum_level.objects.get(id=19)
    consume_level2014 = Consum_level.objects.get(id=20)
    consume_level2015 = Consum_level.objects.get(id=21)
    consume_level2016 = Consum_level.objects.get(id=22)
    consume_level2017 = Consum_level.objects.get(id=23)

    print(consume_level2017.town_people)

    radius = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
    polar = Polar("各年份居民消费水平对比图", width=1500, height=600)
    t1 = int(consume_level2011.town_people)
    t2 = int(consume_level2012.town_people)
    t3 = int(consume_level2013.town_people)
    t4 = int(consume_level2014.town_people)
    t5 = int(consume_level2015.town_people)
    t6 = int(consume_level2016.town_people)
    t7 = int(consume_level2017.town_people)

    c1 = int(consume_level2011.countryside_people)
    c2 = int(consume_level2012.countryside_people)
    c3 = int(consume_level2013.countryside_people)
    c4 = int(consume_level2014.countryside_people)
    c5 = int(consume_level2015.countryside_people)
    c6 = int(consume_level2016.countryside_people)
    c7 = int(consume_level2017.countryside_people)

    b1 = float(consume_level2011.balance)
    b2 = float(consume_level2012.balance)
    b3 = float(consume_level2013.balance)
    b4 = float(consume_level2014.balance)
    b5 = float(consume_level2015.balance)
    b6 = float(consume_level2016.balance)
    b7 = float(consume_level2017.balance)


    polar.add(
        "城市居民",
        [t1,t2,t3,t4,t5,t6,t7],
        radius_data=radius,
        type="barRadius",
        is_stack=True,
    )
    polar.add(
        "农村居民",
        [c1,c2,c3,c4,c5,c6,c7],
        radius_data=radius,
        type="barRadius",
        is_stack=True,
    )
    polar.add(
        "城市农村消费水平对比(农村=1)",
        [b1,b2,b3,b4,b5,b6,b7],
        radius_data=radius,
        type="barRadius",
        is_stack=True,
    )
    polar.render(path="F:/尚世康资料/尚世康+毕业论文相关资料/系统设计/cms/templates/各年份城市农村.html")

    return HttpResponse("各年份城市农村居民消费水平图生成成功")

#2017年全国各地区居民消费水平对比
def Duibi(request):


    attr = ["北京", "天津", "河北", "山西", "内蒙古", "辽宁",
            "吉林", "黑龙江", "上海", "江苏", "浙江", "安徽", "福建",
            "江西", "山东", "河南", "湖北", "湖南", "广东", "广西",
            "海南", "重庆", "四川", "贵州", "云南", "西藏", "陕西", "甘肃",
            "青海", "宁夏", "新疆"]
    L1 = int(Consum_level.objects.filter(year=2017,city="北京")[0].all_people)
    L2 = int(Consum_level.objects.filter(year=2017, city="天津")[0].all_people)
    L3 = int(Consum_level.objects.filter(year=2017, city="河北")[0].all_people)
    L4 = int(Consum_level.objects.filter(year=2017, city="山西")[0].all_people)
    L5 = int(Consum_level.objects.filter(year=2017, city="内蒙古")[0].all_people)
    L6 = int(Consum_level.objects.filter(year=2017, city="辽宁")[0].all_people)
    L7 = int(Consum_level.objects.filter(year=2017, city="吉林")[0].all_people)
    L8 = int(Consum_level.objects.filter(year=2017, city="黒龙江")[0].all_people)
    L9 = int(Consum_level.objects.filter(year=2017, city="上海")[0].all_people)
    L10 = int(Consum_level.objects.filter(year=2017, city="江苏")[0].all_people)
    L11 = int(Consum_level.objects.filter(year=2017, city="浙江")[0].all_people)
    L12 = int(Consum_level.objects.filter(year=2017, city="安徽")[0].all_people)
    L13 = int(Consum_level.objects.filter(year=2017, city="福建")[0].all_people)
    L14 = int(Consum_level.objects.filter(year=2017, city="江西")[0].all_people)
    L15 = int(Consum_level.objects.filter(year=2017, city="山东")[0].all_people)
    L16 = int(Consum_level.objects.filter(year=2017, city="河南")[0].all_people)
    L17 = int(Consum_level.objects.filter(year=2017, city="湖北")[0].all_people)
    L18 = int(Consum_level.objects.filter(year=2017, city="湖南")[0].all_people)
    L19 = int(Consum_level.objects.filter(year=2017, city="广东")[0].all_people)
    L20 = int(Consum_level.objects.filter(year=2017, city="广西")[0].all_people)
    L21 = int(Consum_level.objects.filter(year=2017, city="海南")[0].all_people)

    L22 = int(Consum_level.objects.filter(year=2017, city="重庆")[0].all_people)
    L23 = int(Consum_level.objects.filter(year=2017, city="四川")[0].all_people)
    L24 = int(Consum_level.objects.filter(year=2017, city="贵州")[0].all_people)
    L25 = int(Consum_level.objects.filter(year=2017, city="云南")[0].all_people)
    L26 = int(Consum_level.objects.filter(year=2017, city="西藏")[0].all_people)
    L27 = int(Consum_level.objects.filter(year=2017, city="陕西")[0].all_people)

    L28 = int(Consum_level.objects.filter(year=2017, city="甘肃")[0].all_people)
    L29 = int(Consum_level.objects.filter(year=2017, city="青海")[0].all_people)
    L30 = int(Consum_level.objects.filter(year=2017, city="宁夏")[0].all_people)

    L31 = int(Consum_level.objects.filter(year=2017, city="新疆")[0].all_people)


    v1 = [L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,
          L16, L17, L18, L19, L20, L21, L22, L23, L24, L25, L26, L27, L28, L29, L30,
          L31]
    pie = Pie("2017年全国各地区居民消费水平对比图",width=1500,height=600, title_pos='center')
    pie.add("", attr, v1, label_text_color=None,
    is_label_show=True,
    legend_orient="vertical",
    legend_pos="left",)
    pie.render(path="F:/尚世康资料/尚世康+毕业论文相关资料/系统设计/cms/templates/2017年全国各地区居民消费水平对比.html")

    return HttpResponse("2017年全国各地区居民消费水平对比图生成成功")