def f(start, finish, komand=''):
    if start == finish and komand.count('*') == 1:
        return 1
    if start > finish:
        return 0
    if komand.count('*') > 1:
        return 0
    return (f(start + 1, finish, komand + "+") +
            f(start + 2, finish, komand + "+") +
            f(start * 2, finish, komand + "*") +
            f(start * 3, finish, komand + "*"))

print(f(1, 11))