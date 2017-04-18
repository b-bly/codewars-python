def doors(n):
    # list of doors and status
    doorsArr = []
    # i is student number
    for i in range(n):
        doorsArr.append(True)
    for i in range(1, n + 1):
        #over doors and change every ith door
        if i <= n/2:
            for j in range(i - 1, n, i):
        #if j (door number) % i (student number)
                if not ((j + 1) % i):
                    doorsArr[j] = not (doorsArr[j])
        else:
            j = i - 1
            doorsArr[j] = not doorsArr[j]
    doorsOpen = n - sum(doorsArr)
    return doorsOpen


doors(5)
