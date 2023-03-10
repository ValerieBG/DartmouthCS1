#O(m+n) where m and n are lengths of d1 and d2 respectively
def find_unique_keys(d1, d2):
    res = []

    #Find keys in d1 that are not in d2
    for k in d1:
        if not k in d2:
            res.append(k)

    #Find keys in d2 that are not in d1
    for k in d2:
        if k not in d1:
            res.append(k)

    return res

d1 = {"a":1, "b":3, "d":3, "e":1}
d2 = {"a":10, "b":-3, "c":40, "d":5, "f":4}
d3 = {"z":100, "y":1}

print(find_unique_keys(d1, d2))