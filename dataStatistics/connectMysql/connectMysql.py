'''
连接Mysql的地址和密码
'''
import pymysql


class ConnectMysql():

    # icms数据库地址
    icmsDb = pymysql.connect(host="192.168.6.200", user="rbdb",
                         password="rbdb0580", db="icms", port=3306)

    # 测试数据库地址
    testDb = testDb = pymysql.connect(host="192.168.6.200", user="rbdb",
                         password="rbdb0580", db="icms_alpha", port=3306)

    # 仿真数据库地址
    liveDb = pymysql.connect(host="192.168.6.200", user="rbdb",
                         password="rbdb0580", db="icms_live", port=3306)