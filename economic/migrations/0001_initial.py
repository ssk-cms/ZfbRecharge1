# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-02-15 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area_gdp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=5, verbose_name='年份')),
                ('beijing', models.CharField(max_length=10, verbose_name='北京')),
                ('tianjin', models.CharField(max_length=10, verbose_name='天津')),
                ('hebei', models.CharField(max_length=10, verbose_name='河北')),
                ('shanxi', models.CharField(max_length=10, verbose_name='山西')),
                ('neimenggu', models.CharField(max_length=10, verbose_name='内蒙古')),
                ('liaoning', models.CharField(max_length=10, verbose_name='辽宁')),
                ('jilin', models.CharField(max_length=10, verbose_name='吉林')),
                ('heilongjiang', models.CharField(max_length=10, verbose_name='黑龙江')),
                ('shanghai', models.CharField(max_length=10, verbose_name='上海')),
                ('jiangsu', models.CharField(max_length=10, verbose_name='江苏')),
                ('zhejiang', models.CharField(max_length=10, verbose_name='浙江')),
                ('anhui', models.CharField(max_length=10, verbose_name='安徽')),
                ('fujian', models.CharField(max_length=10, verbose_name='福建')),
                ('jiangxi', models.CharField(max_length=10, verbose_name='江西')),
                ('shandong', models.CharField(max_length=10, verbose_name='山东')),
                ('henan', models.CharField(max_length=10, verbose_name='河南')),
                ('hubei', models.CharField(max_length=10, verbose_name='湖北')),
                ('hunan', models.CharField(max_length=10, verbose_name='湖南')),
                ('guangdong', models.CharField(max_length=10, verbose_name='广东')),
                ('guangxi', models.CharField(max_length=10, verbose_name='广西')),
                ('hainan', models.CharField(max_length=10, verbose_name='海南')),
                ('chongqing', models.CharField(max_length=10, verbose_name='重庆')),
                ('sichuan', models.CharField(max_length=10, verbose_name='四川')),
                ('guizhou', models.CharField(max_length=10, verbose_name='贵州')),
                ('yunnan', models.CharField(max_length=10, verbose_name='云南')),
                ('xizang', models.CharField(max_length=10, verbose_name='西藏')),
                ('shangxi', models.CharField(max_length=10, verbose_name='陕西')),
                ('gansu', models.CharField(max_length=10, verbose_name='甘肃')),
                ('qinghai', models.CharField(max_length=10, verbose_name='青海')),
                ('ningxia', models.CharField(max_length=10, verbose_name='宁夏')),
                ('xinjiang', models.CharField(max_length=10, verbose_name='新疆')),
            ],
            options={
                'verbose_name': '地区GDP',
                'verbose_name_plural': '地区GDP',
            },
        ),
        migrations.CreateModel(
            name='Consum_level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=5, verbose_name='年份')),
                ('city', models.CharField(max_length=10, verbose_name='城市')),
                ('all_people', models.CharField(max_length=10, verbose_name='全体居民')),
                ('town_people', models.CharField(max_length=10, verbose_name='城镇居民')),
                ('countryside_people', models.CharField(max_length=10, verbose_name='农村居民')),
                ('balance', models.CharField(max_length=10, verbose_name='城乡消费水平对比(农村居民=1)')),
            ],
            options={
                'verbose_name': '居民消费水平',
                'verbose_name_plural': '居民消费水平',
            },
        ),
        migrations.CreateModel(
            name='Gdp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=5, verbose_name='年份')),
                ('gdp', models.CharField(max_length=50, verbose_name='国内生产总值')),
                ('gross', models.CharField(max_length=50, verbose_name='国民总收入')),
                ('first_produce', models.CharField(max_length=50, verbose_name='第一产业')),
                ('second_produce', models.CharField(max_length=50, verbose_name='第二产业')),
                ('third_produce', models.CharField(max_length=50, verbose_name='第三产业')),
                ('nong_lin_yu_muye', models.CharField(max_length=50, verbose_name='农林渔牧业')),
                ('industry', models.CharField(max_length=50, verbose_name='工业')),
                ('construstion', models.CharField(max_length=50, verbose_name='建筑业')),
                ('pifa_lingshouye', models.CharField(max_length=50, verbose_name='批发和零售业')),
                ('traffic', models.CharField(max_length=50, verbose_name='交通运输,仓储和邮政业')),
                ('stay', models.CharField(max_length=50, verbose_name='住宿和餐饮业')),
                ('banking', models.CharField(max_length=50, verbose_name='金融业')),
                ('estate', models.CharField(max_length=50, verbose_name='房地产业')),
                ('other', models.CharField(max_length=50, verbose_name='其他')),
                ('ave_gdp', models.CharField(max_length=50, verbose_name='人均国内生产总值(元)')),
            ],
            options={
                'verbose_name': 'GDP',
                'verbose_name_plural': 'GDP',
            },
        ),
        migrations.CreateModel(
            name='Gdp_compose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=5, verbose_name='年份')),
                ('gdp', models.CharField(max_length=50, verbose_name='国内生产总值')),
                ('first_produce', models.CharField(max_length=50, verbose_name='第一产业')),
                ('second_produce', models.CharField(max_length=50, verbose_name='第二产业')),
                ('third_produce', models.CharField(max_length=50, verbose_name='第三产业')),
                ('nong_lin_yu_muye', models.CharField(max_length=50, verbose_name='农林渔牧业')),
                ('industry', models.CharField(max_length=50, verbose_name='工业')),
                ('construstion', models.CharField(max_length=50, verbose_name='建筑业')),
                ('pifa_lingshouye', models.CharField(max_length=50, verbose_name='批发和零售业')),
                ('traffic', models.CharField(max_length=50, verbose_name='交通运输,仓储和邮政业')),
                ('stay', models.CharField(max_length=50, verbose_name='住宿和餐饮业')),
                ('banking', models.CharField(max_length=50, verbose_name='金融业')),
                ('estate', models.CharField(max_length=50, verbose_name='房地产业')),
                ('other', models.CharField(max_length=50, verbose_name='其他')),
            ],
            options={
                'verbose_name': 'GDP构成',
                'verbose_name_plural': 'GDP构成',
            },
        ),
        migrations.CreateModel(
            name='Gdp_index_number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=5, verbose_name='年份')),
                ('gdp', models.CharField(max_length=50, verbose_name='国内生产总值')),
                ('gross', models.CharField(max_length=50, verbose_name='国民总收入')),
                ('first_produce', models.CharField(max_length=50, verbose_name='第一产业')),
                ('second_produce', models.CharField(max_length=50, verbose_name='第二产业')),
                ('third_produce', models.CharField(max_length=50, verbose_name='第三产业')),
                ('nong_lin_yu_muye', models.CharField(max_length=50, verbose_name='农林渔牧业')),
                ('industry', models.CharField(max_length=50, verbose_name='工业')),
                ('construstion', models.CharField(max_length=50, verbose_name='建筑业')),
                ('pifa_lingshouye', models.CharField(max_length=50, verbose_name='批发和零售业')),
                ('traffic', models.CharField(max_length=50, verbose_name='交通运输,仓储和邮政业')),
                ('stay', models.CharField(max_length=50, verbose_name='住宿和餐饮业')),
                ('banking', models.CharField(max_length=50, verbose_name='金融业')),
                ('estate', models.CharField(max_length=50, verbose_name='房地产业')),
                ('other', models.CharField(max_length=50, verbose_name='其他')),
                ('ave_gdp', models.CharField(max_length=50, verbose_name='人均国内生产总值(元)')),
            ],
            options={
                'verbose_name': 'GDP指数(上一年=100)',
                'verbose_name_plural': 'GDP指数(上一年=100)',
            },
        ),
        migrations.CreateModel(
            name='Gdp_index_year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=5, verbose_name='年份')),
                ('gdp', models.CharField(max_length=50, verbose_name='国内生产总值')),
                ('gross', models.CharField(max_length=50, verbose_name='国民总收入')),
                ('first_produce', models.CharField(max_length=50, verbose_name='第一产业')),
                ('second_produce', models.CharField(max_length=50, verbose_name='第二产业')),
                ('third_produce', models.CharField(max_length=50, verbose_name='第三产业')),
                ('nong_lin_yu_muye', models.CharField(max_length=50, verbose_name='农林渔牧业')),
                ('industry', models.CharField(max_length=50, verbose_name='工业')),
                ('construstion', models.CharField(max_length=50, verbose_name='建筑业')),
                ('pifa_lingshouye', models.CharField(max_length=50, verbose_name='批发和零售业')),
                ('traffic', models.CharField(max_length=50, verbose_name='交通运输,仓储和邮政业')),
                ('stay', models.CharField(max_length=50, verbose_name='住宿和餐饮业')),
                ('banking', models.CharField(max_length=50, verbose_name='金融业')),
                ('estate', models.CharField(max_length=50, verbose_name='房地产业')),
                ('other', models.CharField(max_length=50, verbose_name='其他')),
                ('ave_gdp', models.CharField(max_length=50, verbose_name='人均国内生产总值(元)')),
            ],
            options={
                'verbose_name': 'GDP指数(上一年=1978)',
                'verbose_name_plural': 'GDP指数(上一年=1978)',
            },
        ),
    ]
