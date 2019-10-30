import xlrd
import pymysql


# import importlib
# importlib.reload(sys) #出现呢reload错误使用


def open_excel():
    try:
        book = xlrd.open_workbook("地区生产总值2016.xlsx")  # 文件名，把文件与py文件放在同一目录下
    except:
        print("open excel file failed!")
    try:
        sheet = book.sheet_by_name("Sheet1")  # execl里面的worksheet1
        return sheet
    except:
        print("locate worksheet in excel failed!")


# 连接数据库



def search_count(cursor):

    select = "select count(id) from economic_area_gdp"  # 获取表中xxxxx记录数
    cursor.execute(select)  # 执行sql语句
    line_count = cursor.fetchone()
    print(line_count[0])


def insert_deta(cursor):
    sheet = open_excel()
    # cursor = db.cursor()
    # for i in range(2, 7):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1

    year = 2016  # 取第i行第0列
    # print(year)
    beijing = sheet.cell(8, 2).value  # 取第i行第1列，下面依次类推
    tianjin = sheet.cell(9, 2).value
    hebei = sheet.cell(10, 2).value
    shanxi = sheet.cell(11, 2).value
    neimenggu = sheet.cell(12, 2).value
    liaoning = sheet.cell(13, 2).value
    jilin = sheet.cell(14, 2).value
    heilongjiang = sheet.cell(15, 2).value
    shanghai = sheet.cell(16, 2).value
    jiangsu = sheet.cell(17, 2).value
    zhejiang = sheet.cell(18, 2).value
    anhui = sheet.cell(19, 2).value
    fujian = sheet.cell(20, 2).value
    jiangxi = sheet.cell(21, 2).value
    shandong = sheet.cell(22, 2).value
    henan = sheet.cell(23, 2).value
    hubei = sheet.cell(24, 2).value
    hunan = sheet.cell(25, 2).value
    guangdong = sheet.cell(26, 2).value
    guangxi = sheet.cell(27, 2).value
    hainan = sheet.cell(28, 2).value
    chongqing = sheet.cell(29, 2).value
    sichuan = sheet.cell(30, 2).value
    guizhou = sheet.cell(31, 2).value
    yunnan = sheet.cell(32, 2).value
    xizang = sheet.cell(33, 2).value
    shangxi = sheet.cell(34, 2).value
    gansu = sheet.cell(35, 2).value
    qinghai = sheet.cell(36, 2).value
    ningxia = sheet.cell(37, 2).value
    xinjiang = sheet.cell(38, 2).value



    value = (year,beijing,tianjin,hebei,shanxi,neimenggu,liaoning,jilin,heilongjiang,shanghai,jiangsu,zhejiang,anhui,fujian,jiangxi,shandong,henan,hubei,hunan,guangdong,guangxi,hainan,chongqing,sichuan,guizhou,yunnan,xizang,shangxi,gansu,qinghai,ningxia,xinjiang )
    print(value)
    sql = "INSERT INTO economic_area_gdp(year,beijing,tianjin,hebei,shanxi,neimenggu,liaoning,jilin,heilongjiang,shanghai,jiangsu,zhejiang,anhui,fujian,jiangxi,shandong,henan,hubei,hunan,guangdong,guangxi,hainan,chongqing,sichuan,guizhou,yunnan,xizang,shangxi,gansu,qinghai,ningxia,xinjiang )VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, value)  # 执行sql语句
    db.commit()
    cursor.close()  # 关闭连接



if __name__=='__main__':

    db = pymysql.connect(host="127.0.0.1", user="root",port=5505,
                             password="123456",
                             db="cms",
                             charset='utf8')
    cursor = db.cursor()
    insert_deta(cursor)
    db.close()  # 关闭数据
    print("ok ")





