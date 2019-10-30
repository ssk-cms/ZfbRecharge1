'''
这是一个读取excel表格的工具类
'''
import xlrd


class ReadingExcelData:

    @staticmethod
    def reading_excel_data(excel_name, sheet_name):
        global book
        try:
            book = xlrd.open_workbook(excel_name)  # 文件名，把文件与py文件放在同一目录下
        except Exception as e:
            print(e)
        try:
            sheet = book.sheet_by_name(sheet_name)  # execl里面的worksheet名称
            return sheet
        except Exception as e:
            print(e)
