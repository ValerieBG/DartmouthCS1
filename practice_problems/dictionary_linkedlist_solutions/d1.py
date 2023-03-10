def make_square_dict(glist): #O(n) wheren is length of glist
    res = {}

    for x in glist:
        res[x] = x*x

    return res

print(make_square_dict([2, 3, 5, 1, 4]))