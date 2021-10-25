
t='ABCDEFGHIJKLMNOPQR'
t=tuple(t)

s=(8,8,12,12,10,10,10,12,12,12,12,12,12,10,10,10,10,10)

from  openpyxl   import *
wb = Workbook()
ws=wb.active              

for   i   in   range(len(t)):
     ws.column_dimensions[t[i]].width = s[i]

wb.save("testsize.xlsx")
print("20개 열을 모두 다르게 설정 완료(위의 엑셀을 열어 확인해보세요")
