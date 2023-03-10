#O(m*n) where m is runtime of func and n is length of glist
def make_func_dict(glist, func):
    res = {}

    for x in glist:
        res[x] = func(x)

    return res

def func1(x):
    return x*x

def func2(x):
    return 4*x

print(make_func_dict([2, 3, 5, 1, 4], func1))
print(make_func_dict([2, 3, 5, 1, 4], func2))
