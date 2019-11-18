import win32com.client as win32
import os
fname = "C:\\Users\\94960\\Desktop\\python执行\\订单列表 (8).xls"
excel = win32.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Open(fname)

wb.SaveAs(fname + "x", FileFormat=51)  # FileFormat = 51 is for .xlsx extension
wb.Close()  # FileFormat = 56 is for .xls extension
os.remove(fname)
excel.Application.Quit()