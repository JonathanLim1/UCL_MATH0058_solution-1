import matplotlib.pyplot as plt
import numpy as np
from sympy import Symbol, Poly,diff
from sympy.polys.polytools import poly_from_expr,degree
import seaborn as sns
def wilkinson(x):
    p=np.prod(np.array([x-i for i in range(1,21)]))
    return p
x=Symbol('x')
w=1
for i in range(1,21):
    w=w*(x-i)
#print (w.expand()) #this will expand the polynomial
P,d=poly_from_expr(w.expand()) #This will construct a polynomial 
p=P.all_coeffs()
print(f'This is the coeficient of the Wilkinson polynomial {p}')
# machine_root=np.roots(p)
# print(machine_root)
# print(np.polyval(p,np.arange(1,21,dtype=float)))
epsilon=10**(-10)
p[0]=p[0]+epsilon
act_root=[np.arange(1,21)]
x_1=[ele.real for ele in act_root]
y_1=[ele.imag for ele in act_root]
perturbed_root=np.roots(p)
print(f'This is the zeros for the perturbated polynomial {perturbed_root}')
# norm=np.abs(perturbed_root)
# del_x=np.abs(norm-np.arange(20,0,-1))
# p=[float(i) for i in p]
# yval=np.polyval(p,np.arange(1,21))
# con_number=norm/del_x
# print(max(con_number))
x_2=[ele.real for ele in perturbed_root]
y_2=[ele.imag for ele in perturbed_root]
# x_3=[ele.real for ele in machine_root]
# y_3=[ele.imag for ele in machine_root]
fig=plt.figure(figsize=(8, 8))
plt.scatter(x_1,y_1,marker="o",color='red',label='True result')
plt.scatter(x_2,y_2,marker='x',color='black',label="Pertubated result")
# plt.scatter(x_3,y_3)
plt.xlabel('real_axis')
plt.ylabel('img_axis')
plt.legend()
plt.title("Wilkinson polynomial")
plt.grid()
fig.savefig('result.pdf')


# x=Symbol('x')
# w=1
# for i in range(1,21):
#     w=w*(x-i)
# P,d=poly_from_expr(w.expand())
# p=P.all_coeffs()
# p[0]=p[0]+10**(-10)
# p1=Poly(p,x)
# sum=diff(p1,x)
# coe=sum.coeffs()
# con_num=[]
# for i in range(1,21):
#     value=(i**19*(1+10**(-10)))/(np.polyval(coe,i))
#     con_num.append(value)
# a=[abs(j) for j in con_num ]
# print(f'This is the conditional number for different z: {a}')
# print(f' Hence the maximum is {max(a)}, which come from z={a.index(max(a))+1}. ')