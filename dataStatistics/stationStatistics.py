from dataStatistics.connectMysql.connectMysql import ConnectMysql
from dataStatistics.customSql.SqlFile import CustomSql
from dataStatistics.drawingUtils import lineChart
from dataStatistics.drawingUtils.Rose import Rose

def connectMysql():
    # 打开数据库连接
    db = ConnectMysql().icmsDb
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    # 查询23号每隔半个小时进入换电站的车数量，不包含运输车和摩托车
    sql1 = CustomSql.halfHourCar
    # 查询所有数据每半小时在换电站内的车的数量，不包含摩托车和运输车
    sql4 = CustomSql.carInStation
    # 查询23号进入换电站的车辆类型
    sql2 = CustomSql.carType
    # 查询，每辆车在换电站内所待时间
    sql3 = CustomSql.carInStationTime
    try:
        cur.execute(sql1)  # 查询23号车数据量
        result1 = cur.fetchall()
        lineChart.LineChart.HalfHourLine(None,result1)

        cur.execute(sql2)
        result2 = cur.fetchall()  # 查询23号进入换电站的车辆类型
        Rose.carTypeRose(None,result2)

        cur.execute(sql3)
        result3 = cur.fetchall()  # 查询23号车辆在换电站内待的时间
        Rose.carInStationRose(None,result3)

        cur.execute(sql4)
        result4 = cur.fetchall()  # 查询所有数据，每隔半小时进入换电站车的数量
        lineChart.LineChart.StationLine(None,result4)

    except Exception as e:
        raise e
    finally:
        db.close()  # 关闭连接


if __name__ == "__main__":
    connectMysql()
