#!/usr/bin/python3
#-*- coding : utf-8 -*-
# krd-dsc   作者
# 2019/7/12  17:21  当前时间
'''
6.写一个学生管理系统
----------------------------------------------------------
|                    欢迎进入学生管理系统                   |
|                                                         |
| 1.学生信息录入      2.学生成绩查询     3.查找学生信息      |
| 4.录入学生成绩      5.课程平均值     6.所有学生信息        |
----------------------------------------------------------

学生信息：
学号：      姓名：      性别：     成绩：     电话
'''
import Function
while True:
    print(" "*50,end="\t")
    print("-"*60)
    print(" "*50,end="\t")
    print(" "*15,end="\t")
    print("欢迎进入学生管理系统")
    print(" "*60,end="\t")
    print("1.学生信息录入\t\t\t2.学生成绩查询")
    print(" "*60,end="\t")
    print("3.查找学生信息\t\t\t4.录入学生成绩")
    print(" "*60,end="\t")
    print("5.课程平均值\t\t\t6.所有学生信息")
    print(" "*50,end="\t")
    print("-"*60)
    print(" "*50,end="\t")
    c = input("请选择：")
    if c == '1':
        Function.test()
    if c == '2':
        Function.check()
    if c == '3':
        Function.FindInformation()
    if c == '4':
        Function.EA()
    if c == '5':
        Function.KcAverage()
    if c == '6':
        Function.InformationOverview()







