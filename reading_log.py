## Read in values

import tkinter
from tkinter.filedialog import askopenfilename
filename = askopenfilename()

F=open(filename,'r')
lines = F.readlines()
F.close()

## Making list of the temperatures

Tlist=[]

location1=[i for i,x in enumerate(lines) if ('Temperature' in x) and ('Kelvin' in x) and ('Pressure' in x) and ('Atm' in x)]

for i in location1:
    foundstring=lines[i]
    value=float(foundstring.split()[1])
    Tlist.append(value)

## Making list of the Gibbs free energies

Glist=[]

location2=[i for i,x in enumerate(lines) if ('Sum of electronic and thermal Free Energies' in x)]

for i in location2:
    foundstring=lines[i]
    value=float(foundstring.split()[7])
    Glist.append(value)

#Relative G
relativelist=[]

minvalue=min(x for x in Glist)

for i in range(len(Glist)):
    j=Glist[i]
    inkcalmol=(j-minvalue)*627.5095
    relativelist.append(inkcalmol)

#transposing the matrix

alldata = [Tlist,Glist,relativelist]

ziptransposed=list(map(list,zip(*alldata)))

#writes everything

import os
cwd=os.getcwd()
newdir=cwd+'/'+'data'
if not os.path.exists(newdir):
    os.makedirs(newdir)
os.chdir(newdir)

outfile="data_molecule"
Wf=open(outfile,'w')
for x in ziptransposed:
    Wf.write(' '.join(str(x[i]) for i in range(len(x))))
    Wf.write('\n')

Wf.close
