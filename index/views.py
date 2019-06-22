from __future__ import unicode_literals
from django.shortcuts import render

import math

from django.http import HttpResponse



# Create your views here.
from economic.models import Area_gdp, Gdp, Consum_level


def index(request):
    return render(request,'index/index.html')

def index_brief(request):
    return render(request,'index/brief.html')

#2011中国经济图
def ChinaMap_2011(request):
    # if request.GET["type"] == "html":
    return HttpResponse(open("templates/2011中国经济占比地图.html", "rb"), content_type="text/html")

#2011中国经济图
def ChinaMap_2012(request):
    # if request.GET["type"] == "html":
    return HttpResponse(open("templates/2012中国经济占比地图.html", "rb"), content_type="text/html")

#2011中国经济图
def ChinaMap_2013(request):
    # if request.GET["type"] == "html":
    return HttpResponse(open("templates/2013中国经济占比地图.html", "rb"), content_type="text/html")

#2011中国经济图
def ChinaMap_2014(request):
    # if request.GET["type"] == "html":
    return HttpResponse(open("templates/2014中国经济占比地图.html", "rb"), content_type="text/html")

#2011中国经济图
def ChinaMap_2015(request):
    # if request.GET["type"] == "html":
    return HttpResponse(open("templates/2015中国经济占比地图.html", "rb"), content_type="text/html")

#2011中国经济图
def ChinaMap_2016(request):
    # if request.GET["type"] == "html":
    return HttpResponse(open("templates/2016中国经济占比地图.html", "rb"), content_type="text/html")

#2011中国经济图
def ChinaMap_2017(request):
    # if request.GET["type"] == "html":
    return HttpResponse(open("templates/2017中国经济占比地图.html", "rb"), content_type="text/html")

# 分地区经济柱状图3D版
def Area_3d(request):
    return HttpResponse(open("templates/地区GDP对比柱状图.html", "rb"), content_type="text/html")

#地区经济漏斗图
def LouDou_2011(request):
    return HttpResponse(open("templates/2011年地区经济桶状图.html","rb"),content_type="text/html")

def LouDou_2012(request):
    return HttpResponse(open("templates/2012年地区经济桶状图.html","rb"),content_type="text/html")

def LouDou_2013(request):
    return HttpResponse(open("templates/2013年地区经济桶状图.html","rb"),content_type="text/html")

def LouDou_2014(request):
    return HttpResponse(open("templates/2014年地区经济桶状图.html","rb"),content_type="text/html")

def LouDou_2015(request):
    return HttpResponse(open("templates/2015年地区经济桶状图.html","rb"),content_type="text/html")

def LouDou_2016(request):
    return HttpResponse(open("templates/2016年地区经济桶状图.html","rb"),content_type="text/html")

def LouDou_2017(request):
    return HttpResponse(open("templates/2017年地区经济桶状图.html","rb"),content_type="text/html")

#地区经济信息列表展示
def GDP_message(request):
    number_list_2011 = Area_gdp.objects.get(year=2011)
    number_list_2012 = Area_gdp.objects.get(year=2012)
    number_list_2013 = Area_gdp.objects.get(year=2013)
    number_list_2014 = Area_gdp.objects.get(year=2014)
    number_list_2015 = Area_gdp.objects.get(year=2015)
    number_list_2016 = Area_gdp.objects.get(year=2016)
    number_list_2017 = Area_gdp.objects.get(year=2017)
    number_list = [number_list_2011,number_list_2012,number_list_2013,number_list_2014,
                   number_list_2015,number_list_2016,number_list_2017]
    attr = ["北京", "天津", "河北", "山西", "内蒙古", "辽宁",
            "吉林", "黑龙江", "上海", "江苏", "浙江", "安徽", "福建",
            "江西", "山东", "河南", "湖北", "湖南", "广东", "广西",
            "海南", "重庆", "四川", "贵州", "云南", "西藏", "陕西", "甘肃",
            "青海", "宁夏", "新疆"]
    return render(request,'number_list1.html',locals())

#展示GDP构成及分布图
def Compose(request):
    return HttpResponse(open("templates/GDP分布及构成图.html", "rb"), content_type="text/html")

#GDP构成数据展示
def Compose_list(request):

    compose_list = Gdp.objects.all()

    return render(request,'compose_list.html',locals())

#居民消费水平对比
def Level_year(request):
    return HttpResponse(open("templates/各年份城市农村.html", "rb"), content_type="text/html")

# 居民消费水平数据展示
def Show_level(request):

    consum_list = Consum_level.objects.all()

    return render(request,'level_list.html',locals())

# 2017年全国各地区居民消费水平对比.html

def Duibi(request):
    return HttpResponse(open("templates/2017年全国各地区居民消费水平对比.html", "rb"), content_type="text/html")