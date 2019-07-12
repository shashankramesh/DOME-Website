# importing tkinter
from tkinter import *
import math as mat
import J_search as JS
import factors as f
import lewis
from tkinter import font as tkf

# make the GUI
main = Tk()
main.title("Design of Machine Elements")


hfo = tkf.Font(family = "comic sans", size = "20", weight = "bold", underline = 1)
fo = tkf.Font(family = "Times", size = "12", weight = "bold")
tfo = tkf.Font(family = "Times", size = "12", weight = "bold")
ubfo = tkf.Font(family = "Times", size = "18", weight = "bold")


# Defining all sub routines
def copy():
	#Pitch line velocity
	n = float(N.get())
	d = float(m.get())*float(Z.get())
	print(d)
	V = mat.pi*d*n/60000.0

	#Force
	F = 2000.0*float(Applied_torque.get())/d
	output.insert(END, "Force: "+str(F)+"\n")
	
	#Kv
	Kv = f.KV(V, float(Q.get()), "SI")
	output.insert(END, "Velocity factor(Kv): "+str(Kv)+"\n")
	
	#Ko
	Ko = f.KO(str(po.get()),str(so.get()))
	output.insert(END, "Overload Factor (Ko): "+str(Ko)+"\n")

	#Ks
	#Lewis factor
	Y=lewis.Y(int(Z.get()))
	Ks = f.KS(float(b.get()), Y, float(m.get()), "SI")
	output.insert(END, "Size Factor (Ks): "+str(Ks)+"\n")
	
	#Kh
	Dp = float(m.get())*float(Zp.get())
	Kh = f.KM(str(tt.get()), float(S1.get()), float(S.get()), float(b.get()), "SI", str(enc.get()), Dp)
	output.insert(END, "Rim thickness Factor (Kh): "+str(Kh)+"\n")
	
	#Kb
	Kb = 1.0
	
	#Spur Geometry Factor
	Zg = float(Zp.get())*float(m_G.get())
	J = JS.J(int(Zp.get()), Zg)
	output.insert(END, "Bending Geometry Factor (J): "+str(J)+"\n")
	
	#I
	I = f.I(20.0, float(m_G.get()), str(gt.get()))
	output.insert(END, "Pitting Geometry Factor (I): "+str(I)+"\n")
	
	#Cp
	Cp = f.CP("Steel", "Steel")
	output.insert(END, "Cp: "+str(Cp)+"\n")
		
	#KR
	Kr = f.KR(float(R.get()))
	output.insert(END, "Kr: "+str(Kr)+"\n")
	
	#CH
	Ch = f.CH(float(HBp.get()),float(HBg.get()),float(m_G.get()))
	output.insert(END, "Chp: "+str(Ch[0])+"\n"+"Chg: "+str(Ch[1])+"\n")
	
	#YN
	Yn =f.YN(int(NCS.get()))
	output.insert(END, "Yn: "+str(Yn)+"\n")
	
	#ZN
	Zn =f.ZN(int(NCS.get()))
	output.insert(END, "Zn: "+str(Zn)+"\n")
	
	#St,Sc
	S_tot= f.S(str(grade.get()),str(ma.get()),float(HB.get()),"SI")
	output.insert(END, "St: "+str(S_tot[0])+"\n"+"Sc: "+str(S_tot[1])+"\n")
		
	#Bending Stress
	sigB = F*Ko*Kv*Ks*Kh*Kb/(float(m.get())*float(b.get())*J)
	output.insert(END, "Bending Stress: "+str(sigB)+"\n")
	
	#Pitting Stress
	sigC = Cp*mat.sqrt(F*Ko*Kv*Ks*Kh/(Dp*float(b.get())*I))
	output.insert(END, "Pitting Stress: "+str(sigC)+"\n")
	
	#Bending Factor of safety
	Sf = S_tot[0]*Yn/(sigB*Kr)
	output.insert(END, "Bending Factor of Safety: "+str(Sf)+"\n")
	
	#Pitting Factor of safety
	Sh = S_tot[1]*Yn*Ch[1]/(sigC*Kr)
	output.insert(END, "Pitting Factor of Safety: "+str(Sh)+"\n")
	
	output.insert(END, "\n")
	
# Adding the frame
GUI_Frame =Frame(main,bg='powder blue')
GUI_Frame.grid(row=1,column =0,sticky =W)


# Adding the label
Label(main, text ="Gear Design",font =hfo).grid(row =0,column = 0)

#Parameters of Gear Assembly:
Label(GUI_Frame,text ="Parameters for Gear Assembly",bg ='powder blue', font = ubfo).grid(row =1,column =0)
Label(GUI_Frame,text ="Module(mm) ",bg ='powder blue', font = fo).grid(row =2,column =0)
Label(GUI_Frame,text ="Gear-ratio",bg ='powder blue', font = fo).grid(row =3,column =0)
Label(GUI_Frame,text ="Pinion teeth",bg ="powder blue", font = fo).grid(row=4,column =0)
Label(GUI_Frame,text ="Quality factor",bg ='powder blue', font = fo).grid(row =5,column =0)
Label(GUI_Frame,text ="Power Shock Condition",bg ='powder blue', font = fo).grid(row =6,column =0)
Label(GUI_Frame,text ="Load Shock Condition",bg ='powder blue', font = fo).grid(row =7,column =0)
Label(GUI_Frame,text ="Enclosure",bg ="powder blue", font = fo).grid(row=8,column =0)
Label(GUI_Frame,text ="Reliability",bg ="powder blue", font = fo).grid(row=9,column =0)
Label(GUI_Frame,text = "Pinion Brinell Hardness",bg ='powder blue', font = fo).grid(row =10,column =0)
Label(GUI_Frame,text = "Gear Brinell Hardness",bg ='powder blue', font = fo).grid(row =11,column =0)

#Parameters of Gear:
Label(GUI_Frame,text ="Parameters for Gear",bg ='powder blue', font = ubfo).grid(row =12,column =0)
Label(GUI_Frame,text ="Applied Torque(Nm)",bg ='powder blue', font = fo).grid(row =13,column =0)
Label(GUI_Frame,text ="Speed(rpm)",bg ='powder blue', font = fo).grid(row =14,column =0)
Label(GUI_Frame,text ="Gear Type",bg ="powder blue", font = fo).grid(row=15,column =0)
Label(GUI_Frame,text ="Face width(mm)",bg ='powder blue', font = fo).grid(row =16,column =0)
Label(GUI_Frame,text ="Number of teeth",bg ="powder blue", font = fo).grid(row =17,column=0)
Label(GUI_Frame,text ="Teeth Type",bg ="powder blue", font = fo).grid(row=18,column =0)
Label(GUI_Frame, text="Number of Cycles", bg='powder blue', font = fo).grid(row=19, column=0)
Label(GUI_Frame,text ="Gear Material",bg ='powder blue', font = fo).grid(row = 20,column =0)
Label(GUI_Frame, text="grade", bg='powder blue', font = fo).grid(row=21, column=0)
Label(GUI_Frame,text ="Brinell Hardness",bg ='powder blue', font = fo).grid(row = 22,column =0)
Label(GUI_Frame,text ="Mounting Parameters",bg ='powder blue', font = fo).grid(row = 23,column =0)
Label(GUI_Frame,text ="S",bg ="powder blue", font = fo).grid(row = 24,column =0)
Label(GUI_Frame,text ="S1",bg ="powder blue", font = fo).grid(row = 24,column =2)
	#============ Adding input boxes==================================#
	
#Applied torque
temp1_val=StringVar()
temp2_val=StringVar()
temp3_val=StringVar()
temp4_val=StringVar()
temp5_val=StringVar()
temp6_val=StringVar()
temp7_val=StringVar()
temp8_val=StringVar()
temp9_val=StringVar()
temp10_val=StringVar()
temp11_val=StringVar()
temp12_val=StringVar()
temp13_val=StringVar()
temp14_val=StringVar()
temp15_val=StringVar()
temp1_val.set("2")
temp2_val.set("500")
temp3_val.set("1")
temp4_val.set("10")
temp5_val.set("8")
temp6_val.set("2")
temp7_val.set("200")
temp8_val.set("20")
temp9_val.set("0.98")
temp10_val.set("1")
temp11_val.set("1")
temp12_val.set("16")
temp13_val.set("250")
temp14_val.set("300")
temp15_val.set("10000000")
Applied_torque = Entry(GUI_Frame, width =20, bg = 'light grey',textvariable=temp1_val)
Applied_torque.grid(row =13,column =1)

#speed in rpm
N = Entry(GUI_Frame,width =20,bg = 'light grey',textvariable=temp2_val)
N.grid(row =14,column =1)

#module in mm
m = Entry(GUI_Frame,width =20,bg = 'light grey',textvariable=temp3_val)
m.grid(row =2,column =1)

#face width in mm
b = Entry(GUI_Frame,width =20,bg = 'light grey',textvariable=temp4_val)
b.grid(row =16,column =1)

# Quality factor
Q = Entry(GUI_Frame,width =20,bg = 'light grey',textvariable=temp5_val)
Q.grid(row = 5,column =1)

#material
#mat = Entry(GUI_Frame,width =20,bg = 'light grey')
#mat.grid(row =6,column =1)
ma =StringVar()
ma.set("HS")
material = OptionMenu(GUI_Frame,ma,"HS","NTHS","NS")
material.grid(row=20,column =1)
material.configure(width =14)

#conditions for Ko
#cond_Ko = Entry(GUI_Frame,width =20,bg = 'light grey')
#cond_Ko.grid(row =7,column =1)
po = StringVar()   # To access the selected value of power
po.set("Uniform")
power = OptionMenu(GUI_Frame,po,"Uniform","LightShock","MediumShock")
power.grid(row=6,column =1)
power.configure(width =14)

#power.configure(font =("Arial",12))
so = StringVar()
so.set("Uniform")
source = OptionMenu(GUI_Frame,so,"Uniform","ModerateShock","HeavyShock")
source.grid(row=7,column =1)
source.configure(width = 14)

#Gear ratio
m_G = Entry(GUI_Frame,width =20,bg = 'light grey',textvariable=temp6_val)
m_G.grid(row =3,column =1)

#Brinel Hardness
HB = Entry(GUI_Frame,width =20,bg = 'light grey',textvariable=temp7_val)
HB.grid(row =22,column =1)

#No. of teeth
Z = Entry(GUI_Frame,width =20,bg = 'light grey',textvariable=temp8_val)
Z.grid(row =17,column =1)

#Reliability (to calculate K_R)
R = Entry(GUI_Frame,width =20,bg ="light grey",textvariable=temp9_val)
R.grid(row =9,column =1)

#enclosure type (for determining C_ma)
enc =StringVar()
enc.set("CommercialEnclosed")
Enc =OptionMenu(GUI_Frame,enc,"OpenGearing","CommercialEnclosed","PrecisionEnclosed","ExtraPrecisionEnclosed")
Enc.grid(row =8,column =1)
Enc.configure(width =14)

#teeth type
tt = StringVar()
tt.set("Uncrowned")
TT =OptionMenu(GUI_Frame,tt,"Crowned","Uncrowned")
TT.grid(row =18,column =1)
TT.configure(width =14)

#Mount parameters
S = Entry(GUI_Frame,width =20,bg = 'light grey',textvariable=temp10_val)
S.grid(row =24,column =1)

S1 = Entry(GUI_Frame,width =20,bg = 'light grey',textvariable=temp11_val)
S1.grid(row =24,column =3)

#Pinion Teeth
Zp = Entry(GUI_Frame,width =20,bg = 'light grey',textvariable=temp12_val)
Zp.grid(row =4,column =1)

gt = StringVar()
gt.set("External")
GT = OptionMenu(GUI_Frame,gt,"External", "Internal")
GT.grid(row=15,column =1)
GT.configure(width = 14)


#Brinel Hardness
HBp = Entry(GUI_Frame,width =20,bg = 'light grey',textvariable=temp13_val)
HBp.grid(row =10,column =1)

HBg = Entry(GUI_Frame,width =20,bg = 'light grey',textvariable=temp14_val)
HBg.grid(row =11,column =1)

# number of cycles for failure
NCS = Entry(GUI_Frame, width=20, bg='light grey',textvariable=temp15_val)
NCS.grid(row=19, column=1)

#grade of material
grade =StringVar()
grade.set("g1")
Grade = OptionMenu(GUI_Frame,grade,"g1","g2")
Grade.grid(row=21,column =1)
Grade.configure(width =14)

#=============== Adding output boxes================

output = Text(main,width =50,height =20,bg ="light grey", font = tfo)
output.grid(row =1,column =2)

# Adding button "on clicking this button, the result would be displayed"

btn1 = Button(main,text ='submit',width =10,bg='grey',command =copy, font = fo)
btn1.grid(row =2,column =0)

# Everything goes on here

main.mainloop()
