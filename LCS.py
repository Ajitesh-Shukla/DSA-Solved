a = "AGGTAB"
b = "GXTXAYB"    
len_min=min(len(a), len(b))

def lcs(idx_a, idx_b):
    if idx_a==len(a) or idx_b==len(b):
        return 0
    if a[idx_a]==b[idx_b]:
        return 1+lcs(idx_a+1, idx_b+1)
    else:
        return max(lcs(idx_a+1, idx_b), lcs(idx_a, idx_b+1))

print(lcs(0, 0))