import numpy as np
from sympy import Symbol
from sympy import lambdify
import matplotlib.pyplot as plt
#Nodes that want to be interpolated are given
x=np.array([4,5,6,8,12,17])
y=np.array([1.26,1.38,3,8,9,2])
#The divided differences matrix is defined
empty=np.zeros((len(x),len(x)-1))
dif=np.column_stack((x,np.column_stack((y,empty))))
#Divided differences algorithm is applied
print("-----Divided differences-----")
for j in range(2,len(x)+1):
	for i in range(0,(len(x)+1)-j):
		dif[i][j]=(dif[i+1][j-1]-dif[i][j-1])/(x[i+j-1]-x[i])
print(dif)
#The interpolating polynomial is constructed

def pol(t):
	polynom=dif[0][1]
	prod=1.
	for i in range (2,len(x)+1):
		for k in range(0,i-1):
			prod*=(t-dif[k][0])
		polynom += dif[0][i]*prod
	return polynom

polynom=dif[0][1]
prod=1.
t=Symbol("t")
#Symbolic calculus of the interpolating polynomial
for i in range (2,len(x)+1):
        for k in range(0,i-1):
                prod*=(t-dif[k][0])
        polynom += dif[0][i]*prod
print("The interpolating polynomial is:")
print(polynom)
t=np.linspace(x[0],x[len(x)-1],100)
plt.plot(t,pol(t),color="black",label="Interpolation")
plt.scatter(x,y,color="red",label="Nodes")
plt.ylim(0,2)
plt.title("Newtons interpolation method")
plt.legend()
plt.grid()
plt.show()
