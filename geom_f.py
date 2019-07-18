import pandas as pd
Y = pd.read_excel("helical_gf.xls",index_col=0)

#Helical Gear Geometry Factor for bending
def Y_j(helix,Z):
    i=sum(Y.columns<=Z)
    j=Y.columns
    ro =Y.iloc[int(helix)-5]
    gf =ro[j[i-1]]+(Z-j[i-1])/(j[i]-j[i-1])*(ro[j[i]]-ro[j[i-1]])
    return gf
X =pd.read_excel("helical_mod_gf.xls",index_col=0)

#modified geometric factor
def gm_f(helix,Z) :
    i=sum(X.columns<=Z)
    j=X.columns
    ro =X.iloc[int(helix)-5]
    mgf =ro[j[i-1]]+(Z-j[i-1])/(j[i]-j[i-1])*(ro[j[i]]-ro[j[i-1]])
    return mgf

def tot_Y_j(helix,Z) :
    return Y_j(helix,Z)*gm_f(helix,Z)