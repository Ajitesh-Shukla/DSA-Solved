def powerset(idx, arr, all_combs):
    # base
    if idx>=len(arr):
        return all_combs
    # computation
    new_arr=[]
    for arrays in all_combs:
        new_arr.append(arrays+[arr[idx]])
    print(all_combs+new_arr)
    # To count for duplicates
    return powerset(idx+1, arr, all_combs+new_arr)

print(powerset(0, [0, 0, 1], [[]]))