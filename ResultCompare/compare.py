#!usr/bin/env python3
#-*- coding:utf-8 -*-
"""
version: 1.3
author: hunta

this script will compare two test result xml file of iTest,
find all same case with two different result.
if a case run for two times(for exp. fail at first time, rerun after clear up),
it will take the second result to compare.
no clear-up case result

change log:
1.1: the latest result include abort, fail, error(except pass)
1.2: delete abort entries if abort at the both times
1.3: support combine several result summary to one
"""
import re
from bs4 import BeautifulSoup
import xlsxwriter


def error_flag(self):
    if error_flag is True:
        print('there is an error')


def create_table(soup):
    result = []
    table = []
    case = soup.find_all(text=re.compile('test_cases'))
    v = soup.select('a')
    #取出 pass,fail,abort 合并成列表
    for i in range(0, len(v)):
        x = str(v[i]).split('>')
        result.append(x[1])
    # case 和 result 的数目,应相同,一一对应组成 table1
    for i in range(0, len(v)):
        if len(case) != len(v):
            error_flag(True)
        else:
            table.append([case[i],result[i]])
    return table


#将列表 table 转化成 dict
def list_to_dict(table):
    dict = {}
    for i in range(0, len(table)):
        dict[table[i][0]]= table[i][1]
    return dict


#抓取最新一次结果是 fail 和 abort 的 case,
def compare_dict(result_1, result_2):
    differences = {}
    for key in result_2.keys():
        if key in result_1.keys():
            if result_2[key] != 'Pass</a':
                differences[key]=[result_1[key], result_2[key]]
    for key in list(differences.keys()):
        if differences[key][0] == differences[key][1] == 'Abort</a':
            del differences[key]
    return differences


if __name__ == '__main__':
    #输入xml 路径,可输入多次,会将结果合并后再比较
    table_1 = []
    while True:
        names = locals()
        i = 1
        names['1xml%s'% i] = input('请输入上次运行结果的路径: ')
        names['1soup%s' % i] = BeautifulSoup(open(names['1xml%s'% i]), 'lxml')
        names['1table%s' % i] = create_table(names['1soup%s' % i])
        table_1 += names['1table%s' % i]
        tag = input('是否还要添加脚本结果? Y/N: ')
        if tag == 'y' or tag == 'Y':
            i += 1
        else:
            break

    table_2 = []
    while True:
        names = locals()
        i = 1
        names['2xml%s'% i] = input('请输入这次运行结果的路径: ')
        names['2soup%s' % i] = BeautifulSoup(open(names['2xml%s'% i]), 'lxml')
        names['2table%s' % i] = create_table(names['2soup%s' % i])
        table_2 += names['2table%s' % i]
        tag = input('是否还要添加脚本结果? Y/N: ')
        if tag == 'y' or tag == 'Y':
            i += 1
        else:
            break

#    soup_1 = BeautifulSoup(open(xml1), 'lxml')
#    soup_2 = BeautifulSoup(open(xml2), 'lxml')
#    table_1 = create_table(soup_1)
#    table_2 = create_table(soup_2)

    #转化 list 到 dict
    dict_1 = list_to_dict(table_1)
    dict_2 = list_to_dict(table_2)

    print('上一次运行的 case 数目为  %s' % len(dict_1))
    print('这一次运行的 case 数目为  %s' % len(dict_2))
    #比较,生成不同结果的字典
    print('there are %s Failed cases in this time' % len(compare_dict(dict_1, dict_2)))
    dict_content = compare_dict(dict_1, dict_2)
    for s1, s2 in dict_content.items():
        print(s1, s2)

    #将字典导入 excel 文件
    excel_url= input('请输入需要导出的 excel 文件路径(请确保文件存在):')
    book = xlsxwriter.Workbook(excel_url)
    sheet1 = book.add_worksheet()
    num = [k for k in dict_content]
    lennum = len(num)
    for a in range(lennum):
        lena = len(dict_content[num[a]])
        lena1 = dict_content[num[a]]
        try:
            print(lena1)
        except Exception as e:
            print(e)
        a1 = num[a]
        sheet1.write(a + 1, 0, a1)
        b1x = []
        for b in range(lena):
            b1 = (lena1[b])[0]
            b2 = (lena1[b])[1]
            b1x.append(b1)
            sheet1.write(a + 1, b + 1, b1)
        if a == 0:
            for y in range(len(b1x)):
                bx = b1x[y]
                sheet1.write(0, y + 1, bx)
    book.close()