import math
import J_search as JS
import factors as f
import lewis
import sys
import json

'''
	Arguments Format
	Speed --- 1
	Module --- 2
	No_Teeth --- 3
	Torque --- 4
	Quality Factor --- 5
	Units -- 6
	Power -- 7
	Source -- 8
	Face Width -- 9
	Pinion Teeth -- 10
	Enclosure Type -- 11
	S -- 12
	S1 -- 13
	Teeth type -- 14
	gear ratio -- 15
	External/Internal teeth -- 16
	phi -- 17
	Pinion material -- 18
	Gear material -- 19
	Reliability -- 20
	Brinell Hardness Gear -- 21
	Brinell Hardness Pinion -- 22
	No of cycle -- 23
	Brinell Hardness -- 24
	material -- 25
	grade -- 26

'''

#Pitch line velocity
n = float(sys.argv[1]); # SPeed
d = float(sys.argv[2])*float(sys.argv[3])
V = math.pi*d*n/60000.0
out = {'PLVel': V}

#Force
F = 2000.0*float(sys.argv[4])/d
out.update({'Force': F})

#Kv
Kv = f.KV(V, float(sys.argv[5]), str(sys.argv[6]))
out.update({'Kv': Kv})

#Ko
Ko = f.KO(str(sys.argv[7]),str(sys.argv[8]))
out.update({'Ko':Ko})

#Ks
#Lewis factor
Y=lewis.Y(int(sys.argv[3]))
Ks = f.KS(float(sys.argv[9]), Y, float(sys.argv[2]), str(sys.argv[6]))
out.update({'Ks': Ks})

#Kh
Dp = float(sys.argv[2])*float(sys.argv[10])
Kh = f.KM(str(sys.argv[14]), float(sys.argv[13]), float(sys.argv[12]), float(sys.argv[9]), str(sys.argv[6]), str(sys.argv[11]), Dp)
out.update({'Kh': Kh})

#Kb
Kb = 1.0

#Spur Geometry Factor
Zg = float(sys.argv[10])*float(sys.argv[15])
J = JS.J(int(sys.argv[10]), Zg)
out.update({'J': J})

#I
I = f.I(float(sys.argv[17]), float(sys.argv[15]), str(sys.argv[16]))
out.update({'I': I})

#Cp
Cp = f.CP(str(sys.argv[18]), str(sys.argv[19]))
out.update({'Cp': Cp})
	
#KR
Kr = f.KR(float(sys.argv[20]))
out.update({'Kr': Kr})

#CH
Ch = f.CH(float(sys.argv[22]),float(sys.argv[21]), float(sys.argv[15]))
out.update({'Ch': Ch})

#YN
Yn = f.YN(int(sys.argv[23]))
out.update({'Yn': Yn})

#ZN
Zn =f.ZN(int(sys.argv[23]))
out.update({'Zn': Zn})

#St,Sc
S_tot= f.S(str(sys.argv[26]),str(sys.argv[25]),float(sys.argv[24]),str(sys.argv[6]))

#Bending Stress
sigB = F*Ko*Kv*Ks*Kh*Kb/(float(sys.argv[2])*float(sys.argv[9])*J)
out.update({'sigB': sigB})

#Pitting Stress
sigC = Cp*math.sqrt(F*Ko*Kv*Ks*Kh/(Dp*float(sys.argv[9])*I))
out.update({'sigC': sigC})

#Bending Factor of safety
Sf = S_tot[0]*Yn/(sigB*Kr)
out.update({'Sf': Sf})

#Pitting Factor of safety
Sh = S_tot[1]*Yn*Ch[1]/(sigC*Kr)
out.update({'Sh': Sh})

#with open("file.doc","w") as f:
#json.dump(out,open("/home/Desktop/result.json","w")

print(json.dumps(out))

