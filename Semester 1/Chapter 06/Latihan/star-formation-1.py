def starFormation1(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print('* ' , end='')
        print('')

n = int(input('Banyak baris yang akan dicetak : '))
starFormation1(n)
