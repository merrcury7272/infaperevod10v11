# 32x8 + xxx9 = yy02
for p in range(10, 1000):
    for x in range(p):
        for y in range(p):
            x1 = 3*p**3 + 2*p**2 + x*p**1 + 8*p**0
            x2 = x*p**3 + x*p**2 + x*p**1 + 9*p**0
            x3 = y*p**3 + y*p**2 + 0*p**1 + 2*p**0
            if x1 + x2 == x3:
                print(y*p**2 + y*p**1 + x*p**0)
                exit(0)