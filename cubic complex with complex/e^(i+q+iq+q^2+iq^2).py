import math
# q^2
def d(x):
    return ((math.exp(x) - math.exp(-x/2) * math.cos((math.sqrt(3)/2) * x) - 
             math.sqrt(3) * math.exp(-x/2) * math.sin((math.sqrt(3)/2) * x)) / 3)

def b(x):
    return ((math.exp(x) - math.exp(-x/2) * math.cos((math.sqrt(3)/2) * x) + 
             math.sqrt(3) * math.exp(-x/2) * math.sin((math.sqrt(3)/2) * x)) / 3)

def a(x):
    return ((math.exp(x) + 2 * math.exp(-x/2) * math.cos((math.sqrt(3)/2) * x)) / 3)

def c1(t):
    return (math.cos(t)/3 + math.exp((math.sqrt(3) * t)/2) * math.cos(t/2)/3 + 
            math.exp(-(math.sqrt(3) * t)/2) * math.cos(t/2)/3)

def c2(t):
    return ((2 * math.sin(t) + math.exp((-math.sqrt(3)/2) * t) * math.sin(t/2) + 
             math.exp((math.sqrt(3)/2) * t) * math.sin(t/2) - 
             math.sqrt(3) * math.exp((-math.sqrt(3)/2) * t) * math.cos(t/2) + 
             math.sqrt(3) * math.exp((math.sqrt(3)/2) * t) * math.cos(t/2)) / 6)

def c3(t):
    return ((-2 * math.cos(t) + math.exp((-math.sqrt(3)/2) * t) * math.cos(t/2) + 
             math.exp((math.sqrt(3)/2) * t) * math.cos(t/2) - 
             math.sqrt(3) * math.exp((-math.sqrt(3)/2) * t) * math.sin(t/2) + 
             math.sqrt(3) * math.exp((math.sqrt(3)/2) * t) * math.sin(t/2)) / 6)

def c4(t):
    return (-math.sin(t)/3 + math.exp((math.sqrt(3) * t)/2) * math.sin(t/2)/3 + 
            math.exp(-(math.sqrt(3) * t)/2) * math.sin(t/2)/3)

def c5(t):
    return ((2 * math.cos(t) - math.exp((-math.sqrt(3)/2) * t) * math.cos(t/2) - 
             math.exp((math.sqrt(3)/2) * t) * math.cos(t/2) - 
             math.sqrt(3) * math.exp((-math.sqrt(3)/2) * t) * math.sin(t/2) + 
             math.sqrt(3) * math.exp((math.sqrt(3)/2) * t) * math.sin(t/2)) / 6)

def c6(t):
    return ((2 * math.sin(t) + math.exp((-math.sqrt(3)/2) * t) * math.sin(t/2) + 
             math.exp((math.sqrt(3)/2) * t) * math.sin(t/2) + 
             math.sqrt(3) * math.exp((-math.sqrt(3)/2) * t) * math.cos(t/2) - 
             math.sqrt(3) * math.exp((math.sqrt(3)/2) * t) * math.cos(t/2)) / 6)

def s(x, y):
    return a(x) * c1(y) - b(x) * c3(y) + d(x) * c5(y)

def g(x, y):
    return -a(x) * c4(y) + b(x) * c6(y) + d(x) * c2(y)

def h(x, y):
    return a(x) * c3(y) - b(x) * c5(y) - d(x) * c1(y)

def i(x, y):
    return -a(x) * c6(y) - b(x) * c2(y) + d(x) * c4(y)

def j(x, y):
    return a(x) * c5(y) + b(x) * c1(y) - d(x) * c3(y)

def k(x, y):
    return a(x) * c2(y) - b(x) * c4(y) + d(x) * c6(y)
def expq2(x,y):
    a,b,c,d,e,f=s(x, y),g(x, y),h(x, y),i(x, y),j(x, y),k(x, y)
    return a,b,c,d,e,f

#q

def e(x):
    return ((math.exp(-x) - math.exp(x/2) * math.cos((math.sqrt(3)/2) * x) + 
             math.sqrt(3) * math.exp(x/2) * math.sin((math.sqrt(3)/2) * x)) / 3)

def w(x):
    return ((-math.exp(-x) + math.exp(x/2) * math.cos((math.sqrt(3)/2) * x) + 
             math.sqrt(3) * math.exp(x/2) * math.sin((math.sqrt(3)/2) * x)) / 3)

def q(x):
    return ((math.exp(-x) + 2 * math.exp(x/2) * math.cos((math.sqrt(3)/2) * x)) / 3)

def u1(t):
    return (math.cos(t)/3 + math.exp((math.sqrt(3) * t)/2) * math.cos(t/2)/3 + 
            math.exp(-(math.sqrt(3) * t)/2) * math.cos(t/2)/3)

def u3(t):
    return ((-2 * math.cos(t) + math.exp((-math.sqrt(3)/2) * t) * math.cos(t/2) + 
             math.exp((math.sqrt(3)/2) * t) * math.cos(t/2) - 
             math.sqrt(3) * math.exp((-math.sqrt(3)/2) * t) * math.sin(t/2) + 
             math.sqrt(3) * math.exp((math.sqrt(3)/2) * t) * math.sin(t/2)) / 6)

def u2(t):
    return ((2 * math.sin(t) + math.exp((-math.sqrt(3)/2) * t) * math.sin(t/2) + 
             math.exp((math.sqrt(3)/2) * t) * math.sin(t/2) - 
             math.sqrt(3) * math.exp((-math.sqrt(3)/2) * t) * math.cos(t/2) + 
             math.sqrt(3) * math.exp((math.sqrt(3)/2) * t) * math.cos(t/2)) / 6)

def u4(t):
    return (-math.sin(t)/3 + math.exp((math.sqrt(3) * t)/2) * math.sin(t/2)/3 + 
            math.exp(-(math.sqrt(3) * t)/2) * math.sin(t/2)/3)

def u5(t):
    return ((2 * math.cos(t) - math.exp((-math.sqrt(3)/2) * t) * math.cos(t/2) - 
             math.exp((math.sqrt(3)/2) * t) * math.cos(t/2) - 
             math.sqrt(3) * math.exp((-math.sqrt(3)/2) * t) * math.sin(t/2) + 
             math.sqrt(3) * math.exp((math.sqrt(3)/2) * t) * math.sin(t/2)) / 6)

def u6(t):
    return ((2 * math.sin(t) + math.exp((-math.sqrt(3)/2) * t) * math.sin(t/2) + 
             math.exp((math.sqrt(3)/2) * t) * math.sin(t/2) + 
             math.sqrt(3) * math.exp((-math.sqrt(3)/2) * t) * math.cos(t/2) - 
             math.sqrt(3) * math.exp((math.sqrt(3)/2) * t) * math.cos(t/2)) / 6)

def t(x, y):
    return q(x) * u1(y) + w(x) * u3(y) + e(x) * u5(y)

def l(x, y):
    return q(x) * u4(y) + w(x) * u6(y) - e(x) * u2(y)

def z(x, y):
    return -q(x) * u5(y) + w(x) * u1(y) + e(x) * u3(y)

def v(x, y):
    return q(x) * u2(y) + w(x) * u4(y) + e(x) * u6(y)

def m(x, y):
    return -q(x) * u3(y) - w(x) * u5(y) + e(x) * u1(y)

def n(x, y):
    return -q(x) * u6(y) + w(x) * u2(y) + e(x) * u4(y)
def expq1(x,y):
    a,b,c,d,e,f=t(x, y),l(x, y),z(x, y),v(x, y),m(x, y),n(x, y)
    return a,b,c,d,e,f
def expi(x):
    a,b,c,d,e,f = math.cos(x),math.sin(x),0,0,0,0
    return a,b,c,d,e,f 
#addition and mul
def add(m1, m2):
    return tuple(a + b for a, b in zip(m1, m2))

def multiply(m1, m2):
    a1, b1, c1, d1, e1, f1 = m1
    a2, b2, c2, d2, e2, f2 = m2
    
    return (
        a1*a2 - b1*b2 - c1*e2 + d1*f2 - e1*c2 + f1*d2,
        a1*b2 + b1*a2 - c1*f2 - d1*e2 - e1*d2 - f1*c2,
        a1*c2 - b1*d2 + c1*a2 - d1*b2 - e1*e2 + f1*f2,
        a1*d2 + b1*c2 + c1*b2 + d1*a2 - e1*f2 - f1*e2,
        a1*e2 - b1*f2 + c1*c2 - d1*d2 + e1*a2 - f1*b2,
        a1*f2 + b1*e2 + c1*d2 + d1*c2 + e1*b2 + f1*a2
    )

#exp(ai+bq+ciq+dq^2+eiq^2)

def exp(q,w,r,t,v):
    a,b,c,d,e,f = multiply(multiply(expi(q),expq1(w,r)),expq2(t,v))
    return a,b,c,d,e,f

print(exp(1,2,-3,0,2))