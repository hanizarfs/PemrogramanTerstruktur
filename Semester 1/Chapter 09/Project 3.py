def bintang(n):
    space = 2*n-1
    n = (-(-n//2))
    for i in range(0, n):
        print(('*'*(2*i+1)).center(space))
    for i in reversed(range(0, n)):
        print(('*'*(2*i-1)).center(space))
bintang(7)
