import math
from math import exp
from math import sqrt
from math import log
from math import cos
from math import sin
from decimal import Decimal, getcontext

getcontext().prec = 102

def riemann(b,c):
    i=((exp(-b)+2*exp(b/2)*cos(sqrt(3)/2*b))/3)*((exp(c)+2*exp(-c/2)*cos(sqrt(3)/2*c))/3)+((exp(-b)-exp(b/2)*cos(sqrt(3)/2*b)+sqrt(3)*exp(b/2)*sin(sqrt(3)/2*b))/3)*((exp(c)-exp(-c/2)*cos(sqrt(3)/2*c)-sqrt(3)*exp(-c/2)*sin(sqrt(3)/2*c))/3)-((-exp(-b)+exp(b/2)*cos(sqrt(3)/2*b)+sqrt(3)*exp(b/2)*sin(sqrt(3)/2*b))/3)*((exp(c)-exp(-c/2)*cos(sqrt(3)/2*c)+sqrt(3)*exp(-c/2)*sin(sqrt(3)/2*c))/3)
    j=((-exp(-b)+exp(b/2)*cos(sqrt(3)/2*b)+sqrt(3)*exp(b/2)*sin(sqrt(3)/2*b))/3)*((exp(c)+2*exp(-c/2)*cos(sqrt(3)/2*c))/3)-((exp(-b)+2*exp(b/2)*cos(sqrt(3)/2*b))/3)*((exp(c)-exp(-c/2)*cos(sqrt(3)/2*c)-sqrt(3)*exp(-c/2)*sin(sqrt(3)/2*c))/3)-((exp(-b)-exp(b/2)*cos(sqrt(3)/2*b)+sqrt(3)*exp(b/2)*sin(sqrt(3)/2*b))/3)*((exp(c)-exp(-c/2)*cos(sqrt(3)/2*c)+sqrt(3)*exp(-c/2)*sin(sqrt(3)/2*c))/3)
    k=((exp(-b)-exp(b/2)*cos(sqrt(3)/2*b)+sqrt(3)*exp(b/2)*sin(sqrt(3)/2*b))/3)*((exp(c)+2*exp(-c/2)*cos(sqrt(3)/2*c))/3)-((-exp(-b)+exp(b/2)*cos(sqrt(3)/2*b)+sqrt(3)*exp(b/2)*sin(sqrt(3)/2*b))/3)*((exp(c)-exp(-c/2)*cos(sqrt(3)/2*c)-sqrt(3)*exp(-c/2)*sin(sqrt(3)/2*c))/3)+((exp(-b)+2*exp(b/2)*cos(sqrt(3)/2*b))/3)*((exp(c)-exp(-c/2)*cos(sqrt(3)/2*c)+sqrt(3)*exp(-c/2)*sin(sqrt(3)/2*c))/3)
    return i, j, k
a=2
b=0
c=0
total_ta=0
total_tb=0
total_tc=0
for n in range (1,100000):
    d=exp(-a*log(n))
    h=-b*log(n)
    r=-c*log(n)
    i, j, k = riemann(h,r)
    total_ta += i*d
    total_tb += j*d
    total_tc += k*d
print(total_ta,total_tb,total_tc)
    