'''
分析当前总里程数减当天里程数不等于昨天总里程数的数据
'''
from scriptFiles.readingExcelUtils import readingExcelData


def analyze():
    excel_name = "./excelFiles/徐宝安换电记录.xls"
    sheet_name = "Sheet1"
    sheet = readingExcelData.ReadingExcelData.reading_excel_data(excel_name, sheet_name)
    for i in range(1, 679):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
        order_id = sheet.cell(i, 1).value  # 取第i行第2列;orderId
        total_mile = sheet.cell(i, 12).value  # 取第i行第13列;总里程数据
        total_mile_next = sheet.cell(i + 1, 12).value  # 取第i+1行第13列;总里程数据
        tbox_mileage = sheet.cell(i, 13).value  # 取第i行第14列；tbox总里程数据
        real_mileage = sheet.cell(i, 15).value  # 取第i行第15列；当天的真实里程数据

        diffrenceData = int(total_mile) - int(real_mileage)
        print(diffrenceData)
        # 如果总里程数和tbox总里程数不一样，输出orderId到totalmile中
        if int(total_mile) != int(tbox_mileage):
            with open('./resultFile/totalmile.txt', 'a+', encoding="utf-8") as f:
                f.write(
                    '总里程数和tbox总里程数不一样的orderId为' + order_id + "\n" + "\n" + "===============" + "\n")  # 按需更改汉字

        if diffrenceData != int(total_mile_next):
            with open('./resultFile/realmile.txt', 'a+', encoding="utf-8") as f:
                f.write(
                    '当天的总里程减去当天的真实里程不等于昨天的总里程的orderId为' + order_id + "\n" + "\n" + "===============" + "\n")  # 按需更改汉字


if __name__ == '__main__':
    try:
        analyze()
    except Exception as e:
        print(e)
