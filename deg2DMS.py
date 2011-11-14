#!/usr/bin/env python 

import os

def deg2DMS(degree):
    
    """Описание функции deg2DMS()
    Данная функция переводит десятичные градусы в формат Градусы, минуты, секунды"""

    D=int(degree)#Градусы
    M=int((degree-D)*60)#Минуты
    S=round((((degree-D)*60)-M)*60,4)#Секунды
    return D,M,S

def DMS2deg(D,M,S):

    """Описание функции DMS2deg()
    Данная функция переводит градусы в формате Градусы, минуты, секунды в десятичные градусы"""    

    degree=round((S/60+M)/60+D,8)
    return degree

def interval(min,max,x):
    correction_interval=False
    if min<x<max:
        correction_interval=True
    else:
        print "Value out of range, repeat please"
    return correction_interval

#Выбор необходимого действия
choice="0"
while choice != "3":
    correct_choice = False
    while not correct_choice:
        choice=raw_input("\n1. Convert Degree -> Degree, Minutes, Seconds\n\
2. Convert Degree, Minutes, Seconds -> Degree\n\
3. Exit\n\
Select action\n")
        if choice == "1" or choice == "2" or choice == "3":
            correct_choice = True
#            os.system('cls')
        else:
#            os.system('cls')
            print "An incorrect value. Try again\n"

    correct_choice = False
    correct_interval = False
#Если выбрали пересчет Градусы -> Градусы, минуты, секунды
    if choice == "1":
        while correct_choice == False or correct_interval == False:
            try:
                grad = float(raw_input("Enter a value\n"))
                correct_interval=interval(0,180,grad)
                correct_choice = True
            except(ValueError):
                print "An incorrect value. Try again"

        D,M,S=deg2DMS(grad)
        print "%s\xb0=%d\xb0 %d\" %s'" % (grad,D,M,S)

#Если выбрали пересчет Градусы, минуты, секунды -> Градусы
    if choice == "2":
        correct_choice = False
        correct_interval = False
        while correct_choice == False or correct_interval == False:
            try:
                D = int(raw_input("Enter degree\n"))
                correct_interval=interval(0,180,D)
                correct_choice = True
            except(ValueError):
                print "An incorrect value. Try again"
            
        correct_choice = False
        correct_interval = False
        while correct_choice == False:
            try:
                M = int(raw_input("Enter minutes\n"))
                correct_interval=interval(0,60,M)
                correct_choice = True
            except(ValueError):
                print "An incorrect value. Try again"

        correct_choice = False
        correct_interval = False
        while correct_choice == False:
            try:
                S = float(raw_input("Enter seconds\n"))
                correct_interval=interval(0,60,S)
                correct_choice = True
            except(ValueError):
                print "An incorrect value. Try again"
            
        grad=DMS2deg(D,M,S)
        print "%d\xb0 %d\" %s'=%s\xb0" % (D,M,S,grad)
