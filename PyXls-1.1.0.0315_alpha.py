#coding:utf-8

import xlrd
import xlwt
from datetime import datetime

style = xlwt.XFStyle()                      #Settings of writting style
font = xlwt.Font()
font.name = 'SimSun'
style.font = font
style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

ipt = raw_input("Please input:")
ipt = ''.join(ipt.split())
book = (xlrd.open_workbook(ipt))

wb = xlwt.Workbook(encoding='utf-8')
ws = wb.add_sheet('汇总')
first_col = ws.col(0)
first_col.width = 256*15

sh = book.sheet_by_index(0)

day=''
lesson=''

for i in range(0,sh.nrows):
    for j in range(0,sh.ncols):
        if(sh.cell_value(i,j)==u"星期一"):
            a,b=i,j
            print a
            print b
            print sh.cell_value(8,6)
            break

def Lessons (m):
    if (m == 3):
        lesson = u"第一，二节"
    elif (m == 4):
        lesson = u"第三节"
    elif (m == 5):
        lesson = u"第四五节"
    elif (m == 6):
        lesson = u"第六，七节"
    elif (m == 7):
        lesson = u"第八，九节"
    elif (m == 8):
        lesson = u"第10,11,12节"
    return lesson

def Days (n):
    if (n == 2):
        day = u"星期一"
    elif (n == 3):
        day = u"星期二"
    elif (n == 4):
        day = u"星期三"
    elif (n == 5):
        day = u"星期四"
    elif (n == 6):
        day = u"星期五"
    return day

for x in range(0,5):
    ws.write(0,x+1,Days(x+2))

for y in range(0,6):
    ws.write(y+1,0,Lessons(y+3))

for n in range(2,7):
    for m in range(3, 9):
       if(sh.cell_value(m,n)==''):
            lesson = Lessons(m)
            day = Days(n)
            print day + lesson + u"有空"
            ws.write(m-2,n-1,'here')


wb.save('/Users/vilogy/testwt.xls')
