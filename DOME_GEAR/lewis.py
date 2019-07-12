#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:40:30 2019

@author: abhishek,shashank
"""
#importing pandas to read an excel file
import pandas as pd
# lewis.xls consists of Y for different teeth number

def Y(Z):
    lewis =pd.read_excel('lewis.xls')
    Y = float(lewis.Y[lewis["Teeth"]==Z])
    i =sum(lewis.Teeth < Z)
    if Z==12 :
        Y =0.245
    elif Z > 400 :
        Y = 0.485
    else :#for interpolation
        Y = (lewis.Y[i]-lewis.Y[i-1])/(lewis.Teeth[i]-lewis.Teeth[i-1])*(Z-lewis.Teeth[i-1]) +lewis.Y[i-1]
    return Y

