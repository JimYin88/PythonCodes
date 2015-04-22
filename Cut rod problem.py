def cut_rod(p,n):
    r = [0] * (n+1)
    s = [[]] * (n+1)
    print s
    r[0] = 0
    for j in range(1, n+1):
        q = float('-inf')
        for i in range(1,j+1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = [i] + s[j - i]             
        r[j] = q
    return r[n], s[n]
