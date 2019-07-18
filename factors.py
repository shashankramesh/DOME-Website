#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:40:30 2019

@author: abhishek,shashank
"""

import numpy as np
import math
import xlrd

Ko = 0

# Factors
# 1.Dynamic Factor(Kv)
def KV(V,Qv,system):
	B = 0.25*((12.0-Qv)**(2.0/3.0))
	A = 50.0 + 56.0*(1-B)
	if system == 'SI' :
		Kv = ((A+(200.0*V)**(0.5))/A)**(B)     # in m/sec
	elif system == 'US':
		Kv = ((A+(V)**(0.5))/A)**(B)         # in ft/min
	return Kv

# 2. Overload Factor(Ko)
def KO(PS, DM):
	if PS == 'Uniform':					# Here PS = Power Source and DM = Driven Machine
		if DM == 'Uniform':
			Ko = 1.0
		elif DM == 'ModerateShock':
			Ko = 1.25
		elif DM == 'HeavyShock':
			Ko = 1.75
	elif PS == 'LightShock':
		if DM == 'Uniform':
			Ko = 1.25
		elif DM == 'ModerateShock':
			Ko = 1.50
		elif DM == 'HeavyShock':
			Ko = 2.00
	elif PS == 'MediumShock':
		if DM == 'Uniform':
			Ko = 1.5
		elif DM == 'ModerateShock':
			Ko = 1.75
		elif DM == 'HeavyShock':
			Ko = 2.25
	return Ko

# Size Factor(Ks)
def KS(F, Y, P, system):
	if system == 'US':
		Ks = 1.192*((F*(Y)**(0.5))/P)**(0.0535)           # Here F is in Inches and P is Diametral Pitch is in per inch.
	elif system == 'SI':
		b = F
		m = P
		Ks = 0.904*(m*b*(Y)**(0.5))**(0.0535)             # Here b and m are in mm.
	if Ks < 1.0:
		Ks = 1.0									  # Factors should not be less than 1.
	return Ks

#Load Distribution Factor(Km or Kh)               # We will use Km in both SI as well as US.
def KM(Teeth, S1, S, F, system, Condition, Dp):
	# 1. Cmc
	Cmc = 0
	Cpf = 0
	Cpm = 0
	Cma = 0
	Ce = 0
	A = 0
	B = 0
	C = 0
	if Teeth == 'Uncrowned':
		Cmc = 1.0
	elif Teeth == 'Crowned':
		Cmc = 0.8
	# 2. Cpf
	if S1/S < 0.175:                                # Adjustment of bearing
		Cpm = 1.0
	elif S1/S > 0.175 or S1/S == 0.175:
		Cpm = 1.1

	# 3. Cpf
	if system == 'US':
		if F/(10.0*Dp) < 0.025 :                        # Here Dp is in Inches
			Cpf = 1.0
		elif F < 1.0 or F == 1.0 :
			Cpf = F/(10.0*Dp)-0.025
		elif F > 1.0 and (F < 17.0 or F == 17.0):
			Cpf = F/(10.0*Dp)-0.0375+0.0125*F
		elif F > 17.0 and (F < 40.0 or F == 40.0):
			Cpf = F/(10.0*Dp)-0.01109+0.0207*F-0.000228*F*F
	elif system == 'SI':
		b = F
		if b/(10.0*Dp) < 0.025 :
			Cpf = 1.0
		elif b < 25.0 or B == 25.0:
			Cpf = b/(10.0*Dp)-0.025
		elif b > 25.0 and (b < 425.0 or b == 125.0):
			Cpf = b/(10.0*Dp)-0.0375+0.000492*b
		elif b > 17.0 and (b < 40.0 or b == 40.0):
			Cpf = b/(10.0*Dp)-0.01109+0.000815*b-3.53*(10.0**(-7.0))*b*b
	# 4. Cma
	if Condition == 'OpenGearing':
		A = 0.247
		B = 0.0167
		C = -0.0000765
	elif Condition == 'CommercialEnclosed':
		A = 0.127
		B = 0.0158
		C = -0.0000930
	elif Condition == 'PrecisionEnclosed':
		A = 0.0675
		B = 0.0128
		C = -0.0000926
	elif Condition == 'ExtraPrecisionEnclosed':
		A = 0.00360
		B = 0.0102
		C = -0.0000822
	Cma = A + B*F + C*F*F      # F is in Inches, we will co-relate F and b so we always give b and it automatically converted to F.
	# 5. Ce
	Ce = 1.0
	# Just generalized.
	Km = 1.0 + Cmc*(Cpf*Cpm + Cma*Ce)
	return Km

# Rim-Thickness Factor(Kb)                       # mB is backup Ratio
def KB(tR, hT):
	mB = tR/hT
	Kb = 0
	if mB > 1.2 or mB == 1.2:
		Kb = 1.0
	elif mB < 1.2:
		Kb = 1.6*2.303*math.log(2.242/mB,10)
	return Kb

# Surface Geometry Factor for Pitting I or Zi    Note : We will use I in all equations
def I(phi, mG, Type):
	phi = phi*0.0174
	ZI = 0
	if Type == 'Internal':
		ZI = (np.cos(phi)*np.sin(phi)/2.0)*(mG/(mG-1.0))
	elif Type == 'External':
		ZI = (np.cos(phi)*np.sin(phi)/2.0)*(mG/(mG+1.0))
	return ZI

# Elastic Co-efficient(Cp)
def CP(MP, MG):
	workbook = xlrd.open_workbook("J_spur.xls")
	sheet = workbook.sheet_by_index(1)
	
	ng = 1
	while str(sheet.cell_value(0, ng)) != MG:
		ng = ng + 1

	np = 1
	while str(sheet.cell_value(np, 0)) != MP:
		np = np + 1
	
	return sheet.cell_value(np, ng)
	
# Reliability Factor Kr
def KR(R):
	Kr = 1
	if R > 0.5 and (R < 0.99 or R == 0.99):
		Kr = 0.658 - 0.0759*2.303*math.log(1.0-R,10.0)
	elif R > 0.99 and (R < 0.9999 or R is 0.9999):
		Kr = 0.5 - 0.109*2.303*math.log(1.0-R,10.0)
	return Kr

# Hardness Ratio Factor(Ch)
def CH(Hbp, Hbg,mG):
	P = Hbp/Hbg
	S = 0
	if P < 1.2 or P == 1.2:
		S = 0.0
	elif P > 1.2 and (P < 1.7 or P == 1.7):
		S = 0.00898*P-0.00829
	elif P > 1.7 :
		S = 0.00698
	Chg = 1.0 + S*(mG-1.0)
	Chp = 1.0
	return [Chp, Chg]

# Stress Cycle Factor for Bending
def YN(N):
	Yn = 1.6831*(N)**(-0.0323)
	return Yn
	
# Stress Cycle Factor for Pitting
def ZN(N):
	Zn = 2.466*(N)**(-0.056)
	return Zn

# Strength
def S(grade, material, HB, system):
	# For bending
	St = 0
	if material == "HS":
		if grade == "g1":
			St = 0.533*HB + 88.3
		elif grade == "g2":
			St = 0.703*HB + 113.0
	elif material == "NTHS":
		if grade == "g1":
			St = 0.568*HB + 83.8
		elif grade == "g2":
			St = 0.749*HB + 110.0
	elif material == "NS":
		if grade == "g1":
			St = 0.594*HB + 87.76
		elif grade == "g2":
			St = 0.784*HB + 114.81
	
	# For Pitting
	Sc = 0
	if grade == "g1":
		Sc = 2.22*HB + 200.0
	elif grade == "g2":
		Sc = 2.41*HB + 237.0

	# System
	if system == "US":
		St = 145.0*St
		Sc = 145.5*Sc
	
	return [St, Sc]
