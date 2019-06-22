from django.conf.urls import url,include
from economic.views import *
urlpatterns = [
    url(r'^gdp/$', GDP_views,name='GDP'),
    #中国地图地区经济信息生成
    url(r'^number_2011/$',Number_2011,name='number_2011'),
    url(r'^number_2012/$', Number_2012, name='number_2012'),
    url(r'^number_2013/$',Number_2013,name='number_2013'),
    url(r'^number_2014/$',Number_2014,name='number_2014'),
    url(r'^number_2015/$',Number_2015,name='number_2015'),
    url(r'^number_2016/$',Number_2016,name='number_2016'),
    url(r'^number_2017/$',Number_2017,name='number_2017'),
    #3d地区经济信息生成
    url(r'^Zhuzhuangtu3d/$',Zhuzhaungtu3d,name='Zhuzhuangtu3d'),
    #桶装图地区经济信息生成
    url(r'^LouDou_2011/$',LouDou_2011,name='LouDou_2011'),
    url(r'^LouDou_2012/$',LouDou_2012,name='LouDou_2012'),
    url(r'^LouDou_2013/$',LouDou_2013,name='LouDou_2013'),
    url(r'^LouDou_2014/$',LouDou_2014,name='LouDou_2014'),
    url(r'^LouDou_2015/$',LouDou_2015,name='LouDou_2015'),
    url(r'^LouDou_2016/$',LouDou_2016,name='LouDou_2016'),
    url(r'^LouDou_2017/$',LouDou_2017,name='LouDou_2017'),
    #GDP构成及分布生成图
    url(r'^Zhexiantu/$',Zhexiantu,name="Zhexiantu"),
    #各年份农村城市消费水平
    url(r'^Year_level/$',Year_level,name="Year_level"),

    #2017各城市居民消费水平对比图
    url(r'^Duibi/$',Duibi,name="Duibi"),


]