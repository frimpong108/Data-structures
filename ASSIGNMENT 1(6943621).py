L=12 
w=10

#question a1
#for the bending moment and shear force at the first end, x=0
x=0
L=12
w=10
M=(w*(-6*x**2+6*L*x-L**2))/12 #where M is the bending moment
V=w*(0.5*L-x) #where V is the shear force
print('a.')
print(str(M) +  'is the value of the bending moment in kn/m')
print(str(V) +  'is the value of the shear force in m')
#question a2
# for the bending moment and shear forces at the last end, x=L=12
x=L=12
w=10
M=(w*(-6*x**2+6*L*x-L**2))/12 #where M is the bending moment
V=w*(0.5*L-x) #where V is the shear force
print(str(M) +  'is the value of the bending moment in kn/m')
print(str(V) +  'is the value of the shear force in m')
print('')

import numpy as np
#Question b
#at M=0 the expression becomes,x**2-Lx+L**2/6 hence:
a=1    
b=-L
c=L**2/6
#using completing of squares,
discriminant=b**2-4*a*c
root_1=(-b+np.sqrt(discriminant))/2*a
root_2=(-b-np.sqrt(discriminant))/2*a
print('b.')
print(root_1)
print(root_2)
print('')

#Question c
# when the shear force(V)=0 x=L/2
x=L/2
print('c.')
print(str(x) +  'is the value for when the shear force is zero')
print('')

#Question d
d=0
e=12
f=0.01
x=np.arange(d,e,f)
M=(w*(-6*x**2+6*L*x-L**2))/12
print('d.')
print(str(M) + 'are the bending moment values at each step in the array')
print('')

#Question e
x=np.arange(d,e,f)
V=w*(0.5*L-x)
print('e.')
print(str(V) + 'are the shear force vales for each step')
print('')

#Question f
# absolute value of the bending moment is represented by A_M
# minimum absolute value is represented by mA_M 
M=(w*(-6*x**2+6*L*x-L**2))/12
print('f.')
A_M=abs(M)
mA_M=min(A_M)
#when the bending moment is minimum mA_M=M 
#replacing it in the bending moment equation to get x**2-Lx+(L**2/6)+(2*mA_M)/w=0
#comparing to the equation a*X**2+b*x+c
a=1
b=-L
c=(L**2/6)+(2*mA_M)/w
discriminant=b**2-4*a*c
rootf_1=(-b+np.sqrt(discriminant))/2*a
rootf_2=(-b-np.sqrt(discriminant))/2*a
print(rootf_1)
print(rootf_2)
print('')


#Question g
#relative errors is being represented by r.e
r_e_1=(root_1-rootf_1)/root_1*100
r_e_2=(rootf_2-root_2)/rootf_2*100
print('g.')
print(str(r_e_1) + 'and' + str(r_e_2) + 'are the relative errors' )
print('') 

#question H
#let the maximum bending moment be represented by maM and minimum bending moment be MiM
#when bending moment is maximum
maM=max(M)
a=1
b=-L
c=(L**2/6)+(2*maM)/w
discriminant=b**2-4*a*c
root_3=(-b+np.sqrt(discriminant))/2*a
root_4=(-b-np.sqrt(discriminant))/2*a
print('h.')
print('h.' + str(root_3) + 'and'+str(root_4) + 'are the maximum points')
#https://github.com/frimpong108