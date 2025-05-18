from itertools import product

res = 0
for s in product('ЧН', repeat=11):
    s = ''.join(s)
    if s.count("Н") == 3:
        if "НН" not in s:
            if s[0] == "Ч":
                res += 3 * 4 ** 10
            else:
                res += 4 ** 11
            # print(s)
print(res)