#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:40:30 2019

@author: abhishek,shashank
"""
import xlrd
import numpy as np
import math


a1 = 0
a2 = 0
b1 = 0
b2 = 0

def J(Zp, Zg):

	workbook = xlrd.open_workbook("J_spur.xls")
	sheet = workbook.sheet_by_index(0)

	np = 0
	interpolate_p = False
	l_int_p = 16
	l_p = 16
	ng = 0
	interpolate_g = False
	l_int_g = 6
	l_g = 6
	Z = 0
	count = 0
	while count < 2:
		interpolate_p = True
		if Zp < Z:
			np = np - int(l_p/2)
		if Zp > Z:
			np = np + int(l_p/2)
		if Zp is Z:
			interpolate_p = False
		l_int_p = int(l_int_p/2)
		l_p = l_int_p + 1
		if l_p is 1:
			count = count + 1
		Z = int(sheet.cell_value(np, 0))

	count = 0
	Z = 0

	while count < 2:
		interpolate_g = True
		if Zg < Z:
			ng = ng - int(l_g/2)
		if Zg > Z:
			ng = ng + int(l_g/2)
		if Zg is Z:
			interpolate_g = False
		l_int_g = int(l_int_g/2)
		l_g = l_int_g + 1
		if l_g is 1:
			count = count + 1
		Z = int(sheet.cell_value(0, ng))

	if interpolate_g:
		Z = int(sheet.cell_value(0, ng))

		if Zg < Z:
			b1 = ng - 1
			b2 = ng
		else:
			b1 = ng
			b2 = ng + 1

	if interpolate_p:
		Z = int(sheet.cell_value(np, 0))
	
		if Zp < Z:
			a1 = np - 1
			a2 = np
		else:
			a1 = np
			a2 = np + 1
	
	if interpolate_p and interpolate_g:

		J11 = sheet.cell_value(a1, b1)
		J12 = sheet.cell_value(a1, b2)
		J21 = sheet.cell_value(a2, b1)
		J22 = sheet.cell_value(a2, b2)
	
		Zg1 = sheet.cell_value(0, b1)
		Zg2 = sheet.cell_value(0, b2)
	
		Zp1 = sheet.cell_value(a1, 0)
		Zp2 = sheet.cell_value(a2, 0)
	
		J1 = ((float(Zg) - Zg1)*(J12 - J11)/(Zg2 - Zg1)) + J11
		J2 = ((float(Zg) - Zg1)*(J22 - J21)/(Zg2 - Zg1)) + J21
	
		J = math.exp(((math.log(float(Zp)) - math.log(Zp1))*(math.log(J2) - math.log(J1))/(math.log(Zp2) - math.log(Zp1))) + math.log(J1))

	else:
		if interpolate_p:
	
			J1 = sheet.cell_value(a1, ng)
			J2 = sheet.cell_value(a2, ng)
	
			Zp1 = sheet.cell_value(a1, 0)
			Zp2 = sheet.cell_value(a2, 0)
	
			J = math.exp(((math.log(float(Zp)) - math.log(Zp1))*(math.log(J2) - math.log(J1))/(math.log(Zp2) - math.log(Zp1))) + math.log(J1))
		else:
			if interpolate_g:
			
				J1 = sheet.cell_value(np, b1)
				J2 = sheet.cell_value(np, b2)
		
				Zg1 = sheet.cell_value(0, b1)
				Zg2 = sheet.cell_value(0, b2)
	
				J = ((float(Zg) - Zg1)*(J2 - J1)/(Zg2 - Zg1)) + J1
			else:
				J = sheet.cell_value(np, ng)
		
	return J 
	
	
	
	
