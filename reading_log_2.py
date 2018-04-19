print('Program writes out: temperature and Gibbs free energy')

## Read in values

import tkinter
##from tkinter import filedialog
from tkinter.filedialog import askopenfilename
filename = askopenfilename()
#print(filename)

F=open(filename,'r')
lines = F.readlines()
F.close()

## Making list of the temperatures

Tlist=[]

location1=[i for i,x in enumerate(lines) if ('Temperature' in x) and ('Kelvin' in x) and ('Pressure' in x) and ('Atm' in x)]

#print(location1)

#location1=[i for i in enumerate([2,3,4])]
#location1
#[(0, 2), (1, 3), (2, 4)]

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
#    print(value)
    Glist.append(value)

#Relative G
relativelist=[]

minvalue=min(x for x in Glist)

for i in range(len(Glist)):
    j=Glist[i]
    inkcalmol=(j-minvalue)*627.5095
    relativelist.append(inkcalmol)

#numbers = [1,2,3]
#letters = ['a', 'b', 'c']
#ziplist=[numbers,letters]
#print(*ziplist)
#[1, 2, 3] ['a', 'b', 'c']
#list(zip(*ziplist))
#[(3, 0), (4, 1), (5, 2)]
#list(map(list,zip(*ziplist)))
#[[1, 'a'], [2, 'b'], [3, 'c']]
#zipped = zip(numbers, letters)
#print(list(zipped))
#[(1, 'a'), (2, 'b'), (3, 'c')]
#tup2=((4,5),(6,7))
#list(map(list,tup2))
#[[4, 5], [6, 7]]
#def kwa(x):
#    return x**2
#list(map(kwa,[4,5,6]))
#[16, 25, 36]
#list(map(list,(4,5,6,7))) --> 'int' object is not iterable (number '4' cannot be list)

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
#    print(x[0],x[1],x[2])
#    for i in x:
#    Wf.write(' '.join(str(round(x[i],3)) for i in range(len(x))))
    Wf.write(' '.join(str(x[i]) for i in range(len(x))))
    Wf.write('\n')
#Wf.write(' '.join(str(x[i]) for x in ziptransposed))
#Wf.write('\n'.join(str(x) for x in ziptransposed))
#print(' '.join(str(x) for x in ziptransposed))
#for i in ziptransposed:
#Wf.write(str(ziptransposed)+"\n")
#Wf.write(str(ziptransposed[1]))
#Wf.write(str(ziptransposed[2]))
#Wf.write(str(ziptransposed[3]))
Wf.close
