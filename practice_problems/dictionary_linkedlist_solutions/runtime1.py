def func1(glist):
    d = {}

    #Add all values to dictionary and keep the count as value
    for k in glist:
        if k in d:
            d[k] = d[k] + 1
        else:
            d[k] = 1

    #Remove all elements from glist
    #one at a time from the end
    #pop is O(1) so loop below will be O(n)
    #removing from the front will make it O(n^2)
    for i in range(len(glist)):
        glist.pop()

    #Add them back only once
    for k in d:
        if d[k] > 0:
            glist.append(k)
            d[k] = d[k] - 1
