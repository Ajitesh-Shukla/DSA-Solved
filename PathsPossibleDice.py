end=3
def rec(i):
    if i==end:
        return 1
    elif i>end:
        return 0
    res=0
    for j in range(1, 7):
        res+=rec(i+j)
    return res
print(rec(0))