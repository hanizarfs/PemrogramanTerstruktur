import random
def suffleString(x, n):
    randomString = []
    i = 0
    while i < n:
        rand = ''.join(random.sample(x,len(x)))
        if rand in randomString:
            print(end='')
        else:
            randomString.append(rand)
            i+=1
    print(f'randomString {x, n} -> {randomString}')
    
suffleString('aku', 2)
suffleString('aku', 3)
suffleString('aku', 4)
