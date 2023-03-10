#O(n) where n is length of d1
def find_common_keys(d1, d2):
    res = []

    #Find keys in d1 that are not in d2
    for k in d1:
        if k in d2:
            res.append(k)

    return res

d1 = {"a":1, "b":3, "d":3, "e":1}
d2 = {"a":10, "b":-3, "c":40, "d":5, "f":4}
d3 = {"z":100, "y":1}

print(find_common_keys(d2, d1))
