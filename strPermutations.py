str='ABCD'
def permute(i, arr):
    # base
    if i==len(str):
        return arr
    # computation
    ans=[]
    for elem in arr:
        for i in range(len(elem)):
            elem2=elem[:i]+str(i)+elem[i:]
            if
            ans.append(elem2)
    return (i+1, )

    