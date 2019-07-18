#!/usr/bin/python3
#-*- coding : utf-8 -*-
# krd-dsc   作者
# 2019/7/12  19:31  当前时间
#a test module
listStd = []
listStd1 = [] #"学号","姓名","性别","电话","语文成绩","数学成绩","英语成绩","c语言成绩","python成绩"
listStd2 = []
def test():     #学生信息录入
    while True:
        print(" " * 50, end="\t")
        a = input("请输入学号：")
        listStd1.append(a)

        print(" " * 50, end="\t")
        b = input("请输入姓名：")
        listStd1.append(b)
        while True:
            print(" " * 50, end="\t")
            c = input("请输入性别nan/nv：")
            if c == "nan" or c=="nv":
                listStd1.append(c)
                break
            else:
                print(" " * 50, end="\t")
                print("你的输入有误，只能是nan/nv")
                continue
        while True:
            print(" " * 50, end="\t")
            d = input("请输入电话：")
            if len(d) == 8:
                listStd1.append(d)
                break
            else:
                print(" " * 50, end="\t")
                print("你输入的电话号码有误！只能为8位")
                continue

        while True:
            print(" " * 50, end="\t")
            d = int(input("请输入语文成绩："))
            if  d >=0 and d<=150 :
                listStd1.append(d)
                break
            else:
                print(" " * 50, end="\t")
                print("你输入的语文成绩有误！区间[0，150]")
                continue

        while True:
            print(" " * 50, end="\t")
            d = int(input("请输入数学成绩："))
            if  d >=0 and d<=150 :
                listStd1.append(d)
                break
            else:
                print(" " * 50, end="\t")
                print("你输入的数学成绩有误！区间[0，150]")
                continue

        while True:
            print(" " * 50, end="\t")
            d = int(input("请输入英语成绩："))
            if  d >=0 and d<=150 :
                listStd1.append(d)
                break
            else:
                print(" " * 50, end="\t")
                print("你输入的英语成绩有误！区间[0，150]")
                continue

        while True:
            print(" " * 50, end="\t")
            d = int(input("请输入C语言成绩："))
            if  d >=0 and d<=100 :
                listStd1.append(d)
                break
            else:
                print(" " * 50, end="\t")
                print("你输入的c语言成绩有误！区间[0，100]")
                continue

        while True:
            print(" " * 50, end="\t")
            d = int(input("请输入python成绩："))
            if  d >=0 and d<=110 :
                listStd1.append(d)
                break
            else:
                print(" " * 50, end="\t")
                print("你输入的python成绩有误！区间[0，100]")
                continue

        listStd2 = listStd1.copy()
        listStd.append(listStd2)
        listStd1.clear()

        # print(listStd2)
        # print(listStd)
        # print(listStd1)
        print(" " * 50, end="\t")
        print("信息插入成功是否继续插入数据？请选择yes/no")
        print(" " * 50, end="\t")
        e = input()
        if e == "yes":
            continue
        else:
            break
def check():        #查找学生成绩
    while True:
        print(" " * 50, end="\t")
        i = input("请输入学生的学号：")
        for m in listStd:
            if m[0] == i:
                print(" " * 50, end="\t")
                print("你查找的学生成绩为：")
                print(" " * 50, end="\t")
                print("语文成绩：%d"%m[4])
                print(" " * 50, end="\t")
                print("数学成绩：%d"%m[5])
                print(" " * 50, end="\t")
                print("英语成绩：%d"%m[6])
                print(" " * 50, end="\t")
                print("c语言成绩：%d"%m[7])
                print(" " * 50, end="\t")
                print("c语言成绩：%d"%m[8])
                x = 1
                break
            else:
                x = 0
        if x==0:
            print(" " * 50, end="\t")
            print("学号输入有误是否继续查询？请选择yes/no:")
        else:
            print(" " * 50, end="\t")
            print("学生成绩查询成功是否继续查询信息？请选择yes/no:")
        # print(listStd)
        # print(listStd2)
        print(" " * 50, end="\t")
        e = input()
        if e == "yes":
            continue
        else:
            break
def FindInformation(): #查找学生信息
    while True:
        print(" " * 50, end="\t")
        i = input("请输入学生的学号：")
        for m in listStd:
            if i == m[0]:
                print(" " * 50, end="\t")
                print("你查找的学生信息如下:")

                print(" " * 50, end="\t")
                print("学生学号：%s" % m[0])
                print(" " * 50, end="\t")
                print("学生姓名：%s" % m[1])
                print(" " * 50, end="\t")
                print("学生性别：%s" % m[2])
                print(" " * 50, end="\t")
                print("学生电话：%s"% m[3])
                x =1
            else:
                x =0
        if x==0:
            print(" " * 50, end="\t")
            print("学号输入有误是否继续查询？请选择yes/no:")
        else:
            print(" " * 50, end="\t")
            print("学生信息查询成功是否继续查询信息？请选择yes/no:")
        print(" " * 50, end="\t")
        e = input()
        if e == "yes":
            continue
        else:
            break
def EA(): #录入学生成绩
    while True:
        print(" " * 50, end="\t")
        i=input("请需要录入学生的学号：")
        for m in listStd:
            if i == m[0]:
                print(" " * 50, end="\t")
                x = input("请输入需要录入成绩的科目[语文、数学、英语、c语言、python]：")
                if x =="语文":
                    while True:
                        print(" " * 50, end="\t")
                        a = int(input("请输入一个新的成绩："))
                        if a >= 0 and a <= 150:
                            m[4] = a
                            break
                        else:
                            print(" " * 50, end="\t")
                            print("你录入的语文成绩有误！区间[0，150]")
                            continue
                if x =="数学":
                    while True:
                        print(" " * 50, end="\t")
                        b = int(input("请输入一个新的成绩："))
                        if b >= 0 and b <= 150:
                            m[5] = b
                            break
                        else:
                            print(" " * 50, end="\t")
                            print("你录入的数学成绩有误！区间[0，150]")
                            continue
                if x =="英语":
                    while True:
                        print(" " * 50, end="\t")
                        c = int(input("请输入一个新的成绩："))
                        if c >= 0 and c <= 150:
                            m[6] = c
                            break
                        else:
                            print(" " * 50, end="\t")
                            print("你录入的英语成绩有误！区间[0，150]")
                            continue
                if x =="c语言":
                    while True:
                        print(" " * 50, end="\t")
                        d = int(input("请输入一个新的成绩："))
                        if d >= 0 and d <= 100:
                            m[7] = d
                            break
                        else:
                            print(" " * 50, end="\t")
                            print("你录入的c语言成绩有误！区间[0，100]")
                            continue
                if x =="python":
                    while True:
                        print(" " * 50, end="\t")
                        e = int(input("请输入一个新的成绩："))
                        if e >= 0 and e <= 150:
                            m[8] = e
                            break
                        else:
                            print(" " * 50, end="\t")
                            print("你录入的python成绩有误！区间[0，100]")
                            continue
                x = 1
            else:
                x = 0
        if x==0:
            print(" " * 50, end="\t")
            print("学号输入有误是否继续查询？请选择yes/no:")
        else:
            print(" " * 50, end="\t")
            print("学生成绩录入成功是否继续查询信息？请选择yes/no:")
        # print(listStd)
        print(" " * 50, end="\t")
        e = input()
        if e == "yes":
            continue
        else:
            break
def KcAverage():
    while True:
        print(" " * 50, end="\t")
        i = int(input("请输入求平均分课程成绩学生的学号："))
        for m in listStd:
            if i == m[0]:
                print(" " * 50, end="\t")
                print("你查找的学生成绩为：")
                print(" " * 50, end="\t")
                print("语文成绩：%d"%m[4])
                print(" " * 50, end="\t")
                print("数学成绩：%d"%m[5])
                print(" " * 50, end="\t")
                print("英语成绩：%d"%m[6])
                print(" " * 50, end="\t")
                print("c语言成绩：%d"%m[7])
                print(" " * 50, end="\t")
                print("python成绩：%d"%m[8])
                print(" " * 50, end="\t")
                a = int(m[4]+m[5]+m[6]+m[7]+m[8])/5
                print("所有课程的平均成绩为%d"%a)
                x=1
                break
            else:
                x=0
        if x==0:
            print(" " * 50, end="\t")
            print("学号输入有误是否继续查询？请选择yes/no:")
        else:
            print(" " * 50, end="\t")
            print("学生课程平均成绩查询成功是否继续查询信息？请选择yes/no:")
        print(" " * 50, end="\t")
        e = input()
        if e == "yes":
            continue
        else:
            break
def InformationOverview():
    while True:
        print(" " * 50, end="\t")
        print("所有学生信息为：")
        print(" " * 30, end="\t")
        print("*"*138)
        for m in listStd:
            # "学号","姓名","性别","电话","语文成绩","数学成绩","英语成绩","c语言成绩","python成绩"
            print(" " * 30, end="\t")
            print("**\t 学号:%s\t 姓名:%s\t 性别：%s\t 电话：%s\t 语文成绩:%d \t数学成绩:%d\t 英语成绩:%d\t "
                  "c语言成绩:%d\t python成绩:%d\t \t**"% (m[0], m[1], m[2], m[3], m[4], m[5], m[6],m[7],m[8]))
            print(" " * 30, end="\t")
            print("*" * 138)
        e = input("返回请按1")
        if e == "1":
            break
if __name__=='__main__':
    listStd = [[2016,"dsc","nan","88888888",98,78,76,98,79],[2017,"dsq","nan","98888888",96,79,77,94,85]]
    InformationOverview()
