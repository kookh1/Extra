import win32com.client

excel=win32com.client.Dispatch("Excel.Application")
excel.Visible=True
wb=excel.Workbooks.Open('C:\\Users\\kookh\\Desktop\\test.xlsx')
ws=wb.ActiveSheet
print(ws.Cells(1,1).Value)

excel.Quit()