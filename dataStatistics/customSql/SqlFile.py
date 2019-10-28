'''
sql语句
'''

class CustomSql():

    '''
    统计入职中/在职/离职/异常的司机数量
    :return:
    '''
    driverStatus = '''
    SELECT
            company_id AS companyId,
            sum( CASE state WHEN '10' THEN 1 ELSE 0 END ) AS 'toBehired',
            sum( CASE state WHEN '20' THEN 1 ELSE 0 END ) AS 'job',
            sum( CASE state WHEN '30' THEN 1 ELSE 0 END ) AS 'dimission',
            sum( CASE state WHEN '40' THEN 1 ELSE 0 END ) AS 'anomaly'
        FROM
            ic_driver
        WHERE
            1 = 1
        GROUP BY
            company_id'''

    # 查询23号每隔半个小时进入换电站的车数量，不包含运输车和摩托车
    halfHourCar = '''
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
            where  create_date >= "2019-05-23"
            and create_date < "2019-05-24"
            and license_type != "8"
            and license_type != "6"
            ) t
            group  by everyHour,
            everyMinute
            order  by everyHour,
            everyMinute
            '''

    # 查询所有数据每半小时在换电站内的车的数量，不包含摩托车和运输车
    carInStation = '''
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
    carType = '''
        SELECT
            license_type,
            count(1) AS counts
            FROM
            ic_camera_carinfo where create_date >="2019-05-24" and create_date < "2019-05-25"
            GROUP BY
            license_type
    '''

    # 查询，每辆车在换电站内所待时间
    carInStationTime = '''
    select
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

