def line(s, K):  # s координаты точек в ряду
    # K - кол-во точек, которые составляют линию
    cnt = 0
    k = 1
    for i in range(len(s) - 1):
        if s[i + 1] == s[i] + 1:
            k += 1
        elif s[i + 1] == s[i]:
            continue
        elif k >= K:
            cnt += 1
            k = 1
        else:
            k = 1
    if k >= K:
        cnt += 1
    return cnt


with open('26.txt') as f:
    n = int(f.readline())
    k = 3
    data = {}
    s = []
    for i in f.readlines():
        s.append(tuple(map(int, i.split())))
    s.sort()
    for key, values in s:
        try:
            data[key].append(values)
        except:
            data[key] = [values]

maxx = 0
for key, values in data.items():
    if line(values, k) >= maxx:
        maxx = line(values, k)
        row = key
print(maxx, row)
