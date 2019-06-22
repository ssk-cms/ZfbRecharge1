from django.conf.urls import url
from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    #网站简介
    url(r'^brief/$',views.index_brief,name='brief'),
    #中国经济地图2011
    url(r'^chinamap_2011/$',views.ChinaMap_2011,name='chinamap_2011'),
    url(r'^chinamap_2012/$',views.ChinaMap_2012,name='chinamap_2012'),
    url(r'^chinamap_2013/$',views.ChinaMap_2013,name='chinamap_2013'),
    url(r'^chinamap_2014/$',views.ChinaMap_2014,name='chinamap_2014'),
    url(r'^chinamap_2015/$',views.ChinaMap_2015,name='chinamap_2015'),
    url(r'^chinamap_2016/$',views.ChinaMap_2016,name='chinamap_2016'),
    url(r'^chinamap_2017/$',views.ChinaMap_2017,name='chinamap_2017'),
    #分地区的经济信息柱状3d图
    url(r'^Area_3d/$',views.Area_3d,name='Area_3d'),
    #地区经济信息漏斗图
    url(r'^Lou_Dou_2011/$',views.LouDou_2011,name='LouDou_2011'),
    url(r'^Lou_Dou_2012/$',views.LouDou_2012,name='LouDou_2012'),
    url(r'^Lou_Dou_2013/$',views.LouDou_2013,name='LouDou_2013'),
    url(r'^Lou_Dou_2014/$',views.LouDou_2014,name='LouDou_2014'),
    url(r'^Lou_Dou_2015/$',views.LouDou_2015,name='LouDou_2015'),
    url(r'^Lou_Dou_2016/$',views.LouDou_2016,name='LouDou_2016'),
    url(r'^Lou_Dou_2017/$',views.LouDou_2017,name='LouDou_2017'),
    #地区经济信息,以数据展示
    url(r'^number_list1/$',views.GDP_message,name="number_list1"),

    #GDP分布及构成图
    url(r'^compose/$',views.Compose,name="compose"),
    #GDP分布数据展示
    url(r'^compose_list/$',views.Compose_list,name='compose_list'),

    #城市农村对比图
    url(r'^Level_year/$',views.Level_year,name='Level_year'),

    #数据展示
    url(r'^Show_level/$',views.Show_level,name='show_level'),

    # 2017年全国各地区居民消费水平对比.html
    url(r"^Duibi_show/$",views.Duibi,name='Duibi_show'),


]