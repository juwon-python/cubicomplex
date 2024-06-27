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



result =  multiply((1.7601992873180725, 0.5172301336938183, 1.2143458465214998, -1.8667654206099975, -0.4159085230973627, -2.4218103298932707),(2,0,0,0,0,0))
print(result)