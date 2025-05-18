# (3*x + 2y < A) | (y > 15) | (x > 30)

for A in range(1000000):
    f = 1
    for x in range(1050):
        for y in range(1050):
            f *= (3*x + 2*y < A) or (y>15) or (x>30)
        if not f:
            break
    if f:
        print(A)
        break