import pandas as pd
from xlrd import open_workbook
from xlrd import xldate_as_tuple
from datetime import datetime,date
import uuid
import re
import csv


# 过滤空白行模块并过滤不要的数据并写入UUID+正则替换日期格式
# def readUUIDinfo():
#     wb = open_workbook('/media/yucun/软件/苏佼/工作数据/20171120/苏佼20171219 .xlsx')
#     test = open("testkb.txt", 'w+')
#     s = wb.sheets()[3]
#     for row in range(s.nrows):
#         values = []
#         allvalues = []
#         z1 = '年'
#         z2 = '月'
#         uuID = uuid.uuid1()
#         for col in range(s.ncols):
#             values.append(s.cell(row, col).value)
#             strinfo = re.sub('[\.|%s|%s|\/\/]' % (z1, z2), '-', str(values[2]))
#         # strinfo = re.sub('\.','-', str(values[2]))
#         allvalues.append(
#             "insert into {table_name} (sc_data_id, title, company_name, published_date, url) values('%s','%s', '%s', '%s','%s')" % (
#             uuID, str(values[0]), str(values[1]), strinfo, str(values[3])))
#         a = [
#             "insert into {table_name} (sc_data_id, title, company_name, published_date, url) values('%s','', '', '','')" % (
#             uuID)]
#         b = [
#             "insert into {table_name} (sc_data_id, title, company_name, published_date, url) values('%s','行政处罚决定书文号', '违法企业名称或违法自然人姓名', '行政处罚履行方式和期限','')" % (
#             uuID)]
#         c = [
#             "insert into {table_name} (sc_data_id, title, company_name, published_date, url) values('%s','行政处罚决定书文号', '违法企业名称或违法自然人姓名', '行政处罚履行方式和期限','%s')" % (
#             uuID, values[3])]
#         if allvalues == a:
#             continue
#         elif allvalues == b:
#             continue
#         elif allvalues == c:
#             continue
#         else:
#             test.write(str(allvalues) + '\n')
#             # print(id)
#         print(allvalues)



# 复杂表格处理程序demo2 处理数据表一
#处理复
#生成url
def readURl():
    wb = open_workbook('/media/yucun/软件/苏佼/工作数据/20180109/20180110/judgedoc.2018.01.10.xlsx')
    test = open("testURL20180110.txt", 'w+')
    s = wb.sheets()[0]
    fall = ''
    for row in range(s.nrows):
        values = []
        datevalues = []
        URLvalues = []
        uuID = uuid.uuid1()
        for col in range(s.ncols):
            values.append(s.cell(row, col).value)
            # datevalues(xldate_as_tuple(s.cell(row, col).value,wb.datemode))
        strinfo = re.sub('[\.|\/\/]', '-', values[1])
        # URLvalues.append("%s:http://192.168.31.22:3333/api/law/judgedoc/detail/html?docId=%s&trailDate=%s"%(row+1,values[0],strinfo))
        URLvalues.append("http://192.168.31.22:3333/api/law/judgedoc/detail/html?docId=%s&trailDate=%s"%(values[0],strinfo))

        print(URLvalues)
        test.write(str(URLvalues) + '\n')

#生成uptate csv 文件   1
def readUptate():
    wb = open_workbook('/media/yucun/软件/苏佼/工作数据/20180109/20180110/judgedoc.2018.01.10.xlsx')
    test = open("testUptate20180110.csv", 'w+')
    s = wb.sheets()[0]
    for row in range(s.nrows):
        values = []
        Uptatevalues = []
        shu = 1
        for col in range(s.ncols):
            values.append(s.cell(row, col).value)
        strinfo = re.sub('[\.|\/\/]', '-', values[1])
        if "doc_id" != values[0]:
            if "E" != values[5]:
                if "原告" != values[3]:
                    shu = 2
                S = "update judgedoc_litigant set litigant_type = '%s', litigant_type_alias = '%s' where doc_id = '%s' and litigant_name='%s';"% (values[3], shu, values[0], values[2])
                values[6] = S
                test.write(str(values) + '\n')
                # Uptatevalues.to_csv(test.csv)
            else:
                test.write(str(values)+'\n')
        else:
            test.write(str(values) + '\n')

    

#生成uptate csv 文件   2
def readUptate2():
    wb = open_workbook('/media/yucun/软件/苏佼/工作数据/20180109/20180110/judgedoc.2018.01.10.xlsx')
    test = open("testUptate20180110.csv", 'w+')
    writer = csv.writer(test)
    s = wb.sheets()[0]
    for row in range(s.nrows):
        values = []
        Uptatevalues = []
        shu = 1
        for col in range(s.ncols):
            values.append(s.cell(row, col).value)
        strinfo = re.sub('[\.|\/\/]', '-', values[1])
        if "doc_id" != values[0]:
            if "E" != values[5]:
                if "原告" != values[3]:
                    shu = 2
                S = "update judgedoc_litigant set litigant_type = '%s', litigant_type_alias = '%s' where doc_id = '%s' and litigant_name='%s';"% (values[3], shu, values[0], values[2])
                values[6] = S
                writer.writerows(str(values) + '\n')
                # Uptatevalues.to_csv(test.csv)
            else:
                writer.writerows(str(values) + '\n')
        else:
            writer.writerows(str(values)+ '\n')

#生成uptate txt 文件
def readUptatetxt():
    wb = open_workbook('/media/yucun/软件/苏佼/工作数据/20180109/苏佼-20180109裁判文书数据清理(b) .xlsx')
    test = open("testUptate.txt", 'w+')
    s = wb.sheets()[0]
    for row in range(s.nrows):
        values = []
        Uptatevalues = []
        shu = 1
        for col in range(s.ncols):
            values.append(s.cell(row, col).value)
        if "doc_id" != values[0]:
            if "E" != values[5]:
                if "原告" != values[3]:
                    shu = 2
                Uptatevalues.append("update judgedoc_litigant set litigant_type = '%s', litigant_type_alias = '%s' where doc_id = '%s' and litigant_name='%s';"% (values[3], shu, values[0], values[2]))
                # Uptatevalues.to_csv(test.csv)
                test.write(str(Uptatevalues)+'\n')
                print(Uptatevalues)


#生成uptate Sql语句 文件
def readUptateSql():
    wb = open_workbook('/media/yucun/软件/苏佼/工作数据/20180109/20180110/judgedoc.2018.01.10.xlsx')
    test = open("testUptateSql20180110.csv", 'w+')
    s = wb.sheets()[0]
    for row in range(s.nrows):
        values = []
        Uptatevalues = []
        shu = 1
        for col in range(s.ncols):
            values.append(s.cell(row, col).value)
        # strinfo = re.sub('[\.|\/\/]', '-', values[1])
        if "doc_id" != values[0]:
            if "E" != values[5]:
                if "原告" != values[3]:
                    shu = 2
                elif "第三方" == values[3]:
                    shu = 3
                S = "update judgedoc_litigant set litigant_type = '%s', litigant_type_alias = '%s' where doc_id = '%s' and litigant_name='%s';"% (values[3], shu, values[0], values[2])
                test.write(str(S))
            test.write('\n')
                # test.write(str(values) + '\n')


#
def readUUIDalldemo1():
    wb = open_workbook('/media/yucun/软件/苏佼/工作数据/20180109/judgedoc.12.08.xls')
    test = open("testkb1.txt", 'w+')
    s = wb.sheets()[0]
    fall = ''
    for row in range(s.nrows):
        val = []
        values = []
        allvalues = []
        xallvalues = []
        z1 = '年'
        z2 = '月'
        uuID = uuid.uuid1()
        for col in range(s.ncols):
            values.append(s.cell(row, col).value)
        print(values[0])
        a = " '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '', '' " % (
            values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9],values[10],
            values[11], values[12], values[13], values[14], values[15])
        allvalues.append(a)
        # print(allvalues)
        kb = [" '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' "]
        f = [" '%s', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' " % (values[0])]

        lie8 = [" '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '', '', '', '', '', '', '', '', '', '' " % (
            values[0], values[1], values[2], values[3], values[4], values[5], values[6],values[7])]
        lie9 =  [" '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '', '', '', '', '', '', '', '', '' " % (
            values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8])]
        lie10 =[" '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '', '', '', '', '', '', '', '' " % (
                values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9])]
        lie12 = [" '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '', '', '', '', '', '' " % (
                values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9], values[10], values[11])]
        lie15 = [ " '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '', '', '' " % (
                values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8],
                values[9], values[10],values[11],values[12], values[13], values[14])]
        lie16 = [" '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '', '' " % (
                values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8],
                values[9], values[10], values[11], values[12], values[13], values[14], values[15])]
        if allvalues == kb:
            continue
        elif allvalues == f:
            f1 = fall
            pattern = re.compile('[a-zA-Z]')
            # pattern = re.compile('htt*|xxg*')
            if pattern.findall(allvalues[0]):
                fall = values[0]
            else:continue
        elif allvalues == lie8:
            strinfo = re.sub('[\.|%s|%s|\/\/]' % (z1, z2), '-', str(values[5]))
            xallvalues.append("insert into {table_name} (sc_data_id, title, company_name, published_date, url) "
                              "values('%s', '%s', '%s', '%s', '%s','M'" % (uuID,str(values[7]), str(values[1]), strinfo, fall))
            if values[0]!="序\n号":
                test.write(str(xallvalues) + '\n')
            else:continue
        elif allvalues == lie9:
            strinfo = re.sub('[\.|%s|%s|\/\/]' % (z1, z2), '-', str(values[7]))
            xallvalues.append("insert into {table_name} (sc_data_id, title, company_name, published_date, url) "
                              "values('%s', '%s', '%s', '%s', '%s','M'" % (uuID,str(values[1]), str(values[3]), strinfo, fall))
            if values[0]!="序号":
                test.write(str(xallvalues) + '\n')
            else:continue
        elif allvalues == lie10:
            strinfo = re.sub('[\.|%s|%s|\/\/]' % (z1, z2), '-', str(values[8]))
            xallvalues.append("insert into {table_name} (sc_data_id, title, company_name, published_date, url) "
                              "values('%s', '%s', '%s', '%s', '%s','M'" % (uuID,str(values[1]), str(values[3]), strinfo, fall))
            if values[0]!="序号":
                test.write(str(xallvalues) + '\n')
            else:continue
        elif allvalues == lie12:
            strinfo = re.sub('[\.|%s|%s|\/\/]' % (z1, z2), '-', str(values[7]))
            xallvalues.append("insert into {table_name} (sc_data_id, title, company_name, published_date, url) "
                              "values('%s', '%s', '%s', '%s', '%s','M'" % (uuID,str(values[1]), str(values[6]), strinfo, fall))
            if values[0]!="序号":
                test.write(str(xallvalues) + '\n')
            else:continue
        elif allvalues == lie15:
            strinfo = re.sub('[\.|%s|%s|\/\/]' % (z1, z2), '-', str(values[10]))
            xallvalues.append("insert into {table_name} (sc_data_id, title, company_name, published_date, url) "
                              "values('%s', '%s', '%s', '%s', '%s','M'" % (uuID,str(values[1]), str(values[6]), strinfo, fall))
            if values[0]!="序号":
                test.write(str(xallvalues) + '\n')
            else:continue
        elif allvalues == lie16:
            strinfo = re.sub('[\.|%s|%s|\/\/]' % (z1, z2), '-', str(values[11]))
            xallvalues.append("insert into {table_name} (sc_data_id, title, company_name, published_date, url) "
                              "values('%s', '%s', '%s', '%s', '%s','M'" % (uuID,str(values[1]), str(values[7]), strinfo, fall))
            if values[0]!="序号":
                test.write(str(xallvalues) + '\n')
            else:continue
        else:continue


#日期转换
def readURldate():
    wb = open_workbook('/media/yucun/软件/苏佼/工作数据/20180109/20180110/judgedoc.2018.01.10.xlsx')
    test = open("testURL20180110.txt", 'w+')
    s = wb.sheets()[0]
    fall = ''
    for row in range(s.nrows):
        values = []
        datevalues = []
        URLvalues = []
        uuID = uuid.uuid1()
        for col in range(s.ncols):
            values.append(s.cell(row, col).value)
            # datevalues(xldate_as_tuple(s.cell(row, col).value,wb.datemode))
        strinfo = re.sub('[\.|\/\/]', '-', values[1])
        # URLvalues.append("%s:http://192.168.31.22:3333/api/law/judgedoc/detail/html?docId=%s&trailDate=%s"%(row+1,values[0],strinfo))
        URLvalues.append("http://192.168.31.22:3333/api/law/judgedoc/detail/html?docId=%s&trailDate=%s"%(values[0],strinfo))

        print(URLvalues)
        test.write(str(URLvalues) + '\n')





if __name__ == "__main__":
     # readUUIDalldemo1()
    # readUUIDalldemo3()
    # readURl()
    # readUptate()
     readUptateSql()