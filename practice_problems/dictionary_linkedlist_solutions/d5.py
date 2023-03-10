#O(n*n) where is n is length of gdict
#Worst case happens when every key has a unique value

def group_keys_by_vals(gdict):
    res = []

    for k in gdict:
        check = False
        for ilist in res:
            if gdict[ilist[0]] == gdict[k]:
                ilist.append(k)
                check = True

        if not check:
            res.append([k])

    return res

d1  = {"a":1, "b":3, "c":4, "d":3, "e":1, "f": 3}
r = group_keys_by_vals(d1)
print(r)


