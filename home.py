import xlsxwriter

workbook = xlsxwriter.Workbook('main.xlsx')
worksheet = workbook.add_worksheet()
workbook.close()