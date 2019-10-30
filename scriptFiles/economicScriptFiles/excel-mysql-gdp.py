import xlrd
import pymysql


# import importlib
# importlib.reload(sys) #出现呢reload错误使用


def open_excel():
    try:
        book = xlrd.open_workbook("全国经济数据.xlsx")  # 文件名，把文件与py文件放在同一目录下
    except:
        print("open excel file failed!")
    try:
        sheet = book.sheet_by_name("Sheet1")  # execl里面的worksheet1
        return sheet
    except:
        print("locate worksheet in excel failed!")


# 连接数据库

def search_count(cursor):

    select = "select count(id) from economic_gdp"  # 获取表中xxxxx记录数
    cursor.execute(select)  # 执行sql语句
    line_count = cursor.fetchone()
    print(line_count[0])

def insert_deta(cursor):
    sheet = open_excel()
    # cursor = db.cursor()
    for i in range(7, sheet.nrows):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1

        year = sheet.cell(i, 0).value  # 取第i行第0列
        gdp = sheet.cell(i, 1).value  # 取第i行第1列，下面依次类推
        gross = sheet.cell(i, 2).value
        first_produce = sheet.cell(i, 3).value
        second_produce = sheet.cell(i, 4).value
        third_produce = sheet.cell(i, 5).value
        nong_lin_yu_muye = sheet.cell(i, 6).value
        industry = sheet.cell(i, 7).value
        construstion = sheet.cell(i, 8).value
        pifa_lingshouye = sheet.cell(i, 9).value
        traffic = sheet.cell(i, 10).value
        stay = sheet.cell(i, 11).value
        banking = sheet.cell(i, 12).value
        estate = sheet.cell(i, 13).value
        other = sheet.cell(i, 14).value
        ave_gdp = sheet.cell(i, 15).value


        value = (year, gdp,gross,first_produce,second_produce,third_produce,nong_lin_yu_muye,industry,construstion,pifa_lingshouye,traffic,stay,banking,estate,other,ave_gdp)
        print(value)
        sql = "INSERT INTO economic_gdp(year, gdp,gross,first_produce,second_produce,third_produce,nong_lin_yu_muye,industry,construstion,pifa_lingshouye,traffic,stay,banking,estate,other,ave_gdp)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, value)  # 执行sql语句
        db.commit()
    cursor.close()  # 关闭连接



if __name__=='__main__':
    try:
        db = pymysql.connect(host="127.0.0.1", user="root",port=5505,
                             password="123456",
                             db="cms",
                             charset='utf8')
        cursor = db.cursor()
        insert_deta(cursor)
    except:
        print("could not connect to mysql server")



# db.close()  # 关闭数据
print("ok ")