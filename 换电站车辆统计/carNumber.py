import pymysql  # 导入 pymysql
from pyecharts import Line, Pie


def connectMysql():
    # 打开数据库连接
    db = pymysql.connect(host="192.168.6.200", user="rbdb",
                         password="rbdb0580", db="icms", port=3306)

    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    # 查询23号每隔半个小时进入换电站的车数量，不包含运输车和摩托车
    sql1 = '''select
            everyHour,
            everyMinute,
            count(*) as carNumber
            from
            (
            select DATE_FORMAT(create_date,"%H")           as everyHour,
            case
             when DATE_FORMAT (create_date,"%i") >=0 and DATE_FORMAT (create_date,"%i") < 30 then '00'
             when DATE_FORMAT (create_date,"%i") >=30 and DATE_FORMAT (create_date,"%i") < 60 then '30'
            end as everyMinute
            from   ic_camera_carinfo
            where  create_date >= "2019-05-23"
            and create_date < "2019-05-24"
            and license_type != "8"
            and license_type != "6"
            ) t
            group  by everyHour,
            everyMinute
            order  by everyHour,
            everyMinute'''

    # 查询所有数据每半小时在换电站内的车的数量，不包含摩托车和运输车
    sql4 = '''
            select
            everyHour,
            everyMinute,
            count(*) as carNumber
            from
            (
            select DATE_FORMAT(create_date,"%H")           as everyHour,
            case
             when DATE_FORMAT (create_date,"%i") >=0 and DATE_FORMAT (create_date,"%i") < 30 then '00'
             when DATE_FORMAT (create_date,"%i") >=30 and DATE_FORMAT (create_date,"%i") < 60 then '30'
            end as everyMinute
            from   ic_camera_carinfo
            where  
            license_type != "8"
            and license_type != "6"
            ) t
            group  by everyHour,
            everyMinute
            order  by everyHour,
            everyMinute
            '''
    # 查询23号进入换电站的车辆类型
    sql2 = '''SELECT
                license_type,
                count(1) AS counts
                FROM
                ic_camera_carinfo where create_date >="2019-05-24" and create_date < "2019-05-25"
                GROUP BY
                license_type;
    
            '''
    # 查询，每辆车在换电站内所待时间
    sql3 = '''select
            everyMinute,
            count(*) as carNumber
            from
            (
            select 
            case
            when
            (TIME_TO_SEC(modify_date) - TIME_TO_SEC(create_date)) >=0 and  (TIME_TO_SEC(modify_date) - TIME_TO_SEC(create_date)) < 600 then "0-10分钟"   
            when
            (TIME_TO_SEC(modify_date) - TIME_TO_SEC(create_date)) >=600 and  (TIME_TO_SEC(modify_date) - TIME_TO_SEC(create_date)) < 1200 then "10-20分钟" 
            when
            (TIME_TO_SEC(modify_date) - TIME_TO_SEC(create_date)) >=1200 and  (TIME_TO_SEC(modify_date) - TIME_TO_SEC(create_date)) < 1800 then "20-30分钟"
            when
            (TIME_TO_SEC(modify_date) - TIME_TO_SEC(create_date)) >=1800 and  (TIME_TO_SEC(modify_date) - TIME_TO_SEC(create_date)) < 2400 then "30-40分钟"
            when
            (TIME_TO_SEC(modify_date) - TIME_TO_SEC(create_date)) >=2400 and  (TIME_TO_SEC(modify_date) - TIME_TO_SEC(create_date)) < 3000 then "40-50分钟"
            when
            (TIME_TO_SEC(modify_date) - TIME_TO_SEC(create_date)) >=3000 and  (TIME_TO_SEC(modify_date) - TIME_TO_SEC(create_date)) < 3600 then "50-60分钟"
            else "其他"
            end as "everyMinute"         
            from   ic_camera_carinfo
            where  create_date >= "2019-05-23"
            and create_date < "2019-05-24"
            and license_type != "8"
            and license_type != "6"
            ) t
            group  by 
            everyMinute
            order  by 
            everyMinute
    
            '''
    try:
        cur.execute(sql1)  # 查询23号车数据量
        result1 = cur.fetchall()
        Zhexiantu(result1)

        cur.execute(sql2)
        result2= cur.fetchall()  # 查询23号进入换电站的车辆类型
        Shanxing(result2)

        cur.execute(sql3)
        result3 = cur.fetchall()  # 查询23号车辆在换电站内待的时间
        Shanxing2(result3)

        cur.execute(sql4)
        result4 = cur.fetchall()  # 查询所有数据，每隔半小时进入换电站车的数量
        Zhexiantu2(result4)

        # print(result1)
        # print(result2)
        # print("id", "name", "password")
        # 遍历结果
        # for row in results:
        #     hour = row[0]
        #     minute = row[1]
        #     count = row[2]
        #     print(hour,minute,count)
            # print(type(hour), type(minute), type(count))
    except Exception as e:
        raise e
    finally:
        db.close()  # 关闭连接

def Zhexiantu(result1):

    attr1 = []
    v1 = []
    total1 = 0
    for row in result1:
        hour = row[0]
        minute = row[1]
        count = row[2]

        total1 += count

        attr1.append(hour+":"+minute)
        v1.append(count)

    line = Line("24号每半小时换电站内进入车辆信息统计","该日车辆总数为"+str(total1),width=1500,height=600)
    line.add("24号进入换电站车辆数量", attr1, v1, mark_line=["average"],mark_point=["max","min"])
    line.render(path="E:/毕业设计相关资料/cms/换电站车辆统计/24号每隔半小时进入换电站车辆信息统计.html")


def Zhexiantu2(result4):

    attr2 = []
    v2 = []
    total2 = 0
    for row in result4:
        hour = row[0]
        minute = row[1]
        count = row[2]

        total2 += count
        if hour == None and minute == None:
            attr2.append("无时间")
        else:
            attr2.append(hour + ":" + minute)
        v2.append(count)

    line = Line("全部数据分时间段换电站内进入车辆信息统计","车辆总数为"+str(total2),width=1500,height=600)
    line.add("全部数据分时间段进入换电站车辆数量", attr2, v2, mark_line=["max", "average","min"])
    line.render(path="E:/毕业设计相关资料/cms/换电站车辆统计/全部数据每隔半小时进入换电站车辆信息统计.html")


def Shanxing(result2):


    attr = []
    v1 = []

    for row in result2:
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
    pie = Pie("24号车牌类型统计",width=1500,height=600, title_pos='center')
    pie.add("", attr, v1, label_text_color=None,
    is_label_show=True,
    legend_orient="vertical",
    legend_pos="left",)
    pie.render(path="E:/毕业设计相关资料/cms/换电站车辆统计/24号车牌类型统计.html")

def Shanxing2(result3):


    attr = []
    v1 = []

    for row in result3:
        second = row[0]
        count = row[1]
        # print(second)

        attr.append(second)
        v1.append(count)
    pie = Pie("车辆在换电站所待时间信息统计",width=1500,height=600, title_pos='center')
    pie.add("", attr, v1, label_text_color=None,
    is_label_show=True,
    legend_orient="vertical",
    legend_pos="left",)
    pie.render(path="E:/毕业设计相关资料/cms/换电站车辆统计/24号车待的时间统计.html")



if __name__ == "__main__":

    connectMysql()

    '''
    
    '''