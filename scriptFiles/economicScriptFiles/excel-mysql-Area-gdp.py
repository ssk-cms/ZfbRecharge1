import xlrd
import pymysql


# import importlib
# importlib.reload(sys) #出现呢reload错误使用


def open_excel():
    try:
        book = xlrd.open_workbook("地区生产总值2015.xlsx")  # 文件名，把文件与py文件放在同一目录下
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
    for i in range(2, 7):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1

        year = sheet.cell(5, i).value  # 取第i行第0列
        # print(year)
        beijing = sheet.cell(6, i).value  # 取第i行第1列，下面依次类推
        tianjin = sheet.cell(7, i).value
        hebei = sheet.cell(8, i).value
        shanxi = sheet.cell(9, i).value
        neimenggu = sheet.cell(10, i).value
        liaoning = sheet.cell(11, i).value
        jilin = sheet.cell(12, i).value
        heilongjiang = sheet.cell(13, i).value
        shanghai = sheet.cell(14, i).value
        jiangsu = sheet.cell(15, i).value
        zhejiang = sheet.cell(16, i).value
        anhui = sheet.cell(17, i).value
        fujian = sheet.cell(18, i).value
        jiangxi = sheet.cell(19, i).value
        shandong = sheet.cell(20, i).value
        henan = sheet.cell(21, i).value
        hubei = sheet.cell(22, i).value
        hunan = sheet.cell(23, i).value
        guangdong = sheet.cell(24, i).value
        guangxi = sheet.cell(25, i).value
        hainan = sheet.cell(26, i).value
        chongqing = sheet.cell(27, i).value
        sichuan = sheet.cell(28, i).value
        guizhou = sheet.cell(29, i).value
        yunnan = sheet.cell(30, i).value
        xizang = sheet.cell(31, i).value
        shangxi = sheet.cell(32, i).value
        gansu = sheet.cell(33, i).value
        qinghai = sheet.cell(34, i).value
        ningxia = sheet.cell(35, i).value
        xinjiang = sheet.cell(36, i).value



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





