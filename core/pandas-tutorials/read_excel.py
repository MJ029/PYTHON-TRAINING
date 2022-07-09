#first row and column
import openpyxl


path = "../../dataset/File-Handling/Excel-Reading/Data-Generation.xlsx"

wb_obj = openpyxl.load_workbook(path)

sheet_obj = wb_obj.active

cell_obj =sheet_obj.cell(row = 1, column = 1)

print(cell_obj.value)


