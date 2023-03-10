def check_strings(str1, str2):
    print([str1, str2])

    d1 = {}
    for x in str1:
        if x in d1:
            d1[x] = d1[x] + 1
        else:
            d1[x] = 1

    d2 = {}
    for x in str2:
        if x in d2:
            d2[x] = d2[x] + 1
        else:
            d2[x] = 1

    # Check if all characters in str1 are
    # there in str2
    for k in d1:
        if k not in d2:
            return False

    #It is important to check in reverse direction to find keys
    #that are present in d2 but missing in d1
    for k in d2:
        if k not in d1:
            return False

    return True

print(check_strings('dirty room','dormitory'))
print(check_strings('washer', 'dishwasher'))
print(check_strings("to", "too"))