'''
统计司机信息
'''
from dataStatistics.connectMysql.connectMysql import ConnectMysql
from dataStatistics.customSql.SqlFile import CustomSql
from dataStatistics.drawingUtils.Histogram import Histogram
from dataStatistics.drawingUtils.Rose import Rose


def driverStatistics():
    # 打开数据库连接
    db = ConnectMysql().testDb
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    # 查询待入职/在职/离职/异常的司机数量
    sql1 = CustomSql.driverStatus
    try:
        cur.execute(sql1)
        result1 = cur.fetchall()  # 查询23号进入换电站的车辆类型
        print(result1)
        Histogram.driverStatus(None,result1)
    except Exception as e:
        raise e
    finally:
        db.close()  # 关闭连接

if __name__ == "__main__":
    driverStatistics()
