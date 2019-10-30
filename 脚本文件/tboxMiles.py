'''
分析里程数不同的日期
'''
import xlrd


def open_excel():
    try:
        book = xlrd.open_workbook("徐宝安换电记录.xls")  # 文件名，把文件与py文件放在同一目录下
    except:
        print("open excel file failed!")
    try:
        sheet = book.sheet_by_name("Sheet1")  # execl里面的worksheet1
        return sheet
    except:
        print("locate worksheet in excel failed!")


def analyze():
    sheet = open_excel()
    for i in range(1, 679):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
        print(i)
        orderId = sheet.cell(i, 1).value  # 取第i行第2列;orderId
        print(orderId)
        totalMile = sheet.cell(i, 12).value  # 取第i行第13列;总里程数据
        # print(totalMile)
        totalMileNext = sheet.cell(i + 1, 12).value  # 取第i+1行第13列;总里程数据
        # print(totalMileNext)
        tboxMileage = sheet.cell(i, 13).value  # 取第i行第14列；tbox总里程数据
        # print(tboxMileage)
        realMileage = sheet.cell(i, 15).value  # 取第i行第15列；当天的真实里程数据
        # print(realMileage)

        diffrenceData = int(totalMile) - int(realMileage)
        print(diffrenceData)
        # 如果总里程数和tbox总里程数不一样，输出orderId到totalmile中
        if int(totalMile) != int(tboxMileage):
            with open('./resultFile/totalmile.txt', 'a+', encoding="utf-8") as f:
                f.write(
                    '总里程数和tbox总里程数不一样的orderId为'+orderId + "\n" + "\n" + "===============" + "\n")  # 按需更改汉字

        if diffrenceData!= int(totalMileNext):
            with open('./resultFile/realmile.txt', 'a+', encoding="utf-8") as f:
                f.write(
                    '当天的总里程减去当天的真实里程不等于昨天的总里程的orderId为'+orderId + "\n" + "\n" + "===============" + "\n")  # 按需更改汉字


if __name__ == '__main__':
    try:
        analyze()
    except Exception as e:
        print(e)
