import xlrd

wb = xlrd.open_workbook("C:\Users\subbu\Desktop\Book.xlsx")
sheet = wb.sheet_by_index(0)
rows = sheet.nrows
for row in range(rows):
 print sheet.cell_value(row,0) + sheet.cell_value(row,1)
