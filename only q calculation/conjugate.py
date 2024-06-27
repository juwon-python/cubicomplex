def conjugate(m1):
    x1,y1,z1 = m1
    result_x = x1**2+y1*z1
    result_y = -z1**2-x1*y1
    result_z = y1**2-x1*z1
    return (result_x, result_y, result_z)
m1 = (1, 2, 1)

result = conjugate(m1)
print(result)