import xlrd
import pymysql


# import importlib
# importlib.reload(sys) #出现呢reload错误使用


def open_excel():
    try:
        book = xlrd.open_workbook("分地区居民消费水平.xlsx")  # 文件名，把文件与py文件放在同一目录下
    except:
        print("open excel file failed!")
    try:
        sheet = book.sheet_by_name("Sheet1")  # execl里面的worksheet1
        return sheet
    except:
        print("locate worksheet in excel failed!")


# 连接数据库



def search_count(cursor):

    select = "select count(id) from economic_consum_level"  # 获取表中xxxxx记录数
    cursor.execute(select)  # 执行sql语句
    line_count = cursor.fetchone()
    print(line_count[0])


def insert_deta(cursor):
    sheet = open_excel()
    # cursor = db.cursor()
    for i in range(8, 39):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1

        city = sheet.cell(i, 0).value  # 取第i行第0列
        print(city)
        year = 2017
        all_people = sheet.cell(i, 3).value  # 取第i行第1列，下面依次类推
        town_people = sheet.cell(i, 4).value
        countryside_people = sheet.cell(i, 6).value
        balance = sheet.cell(i, 7).value



        value = (year,city,all_people,town_people,countryside_people,balance)
        sql = "INSERT INTO economic_consum_level(year,city,all_people,town_people,countryside_people,balance)VALUES(%s,%s,%s,%s,%s,%s)"
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




