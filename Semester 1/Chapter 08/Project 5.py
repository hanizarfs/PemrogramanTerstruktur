try:
    bil = []
    hasil = []
    def kuadrat(bil):
        for num in bil:
            sqNum = num**2
            hasil.append(sqNum)
    n = int(input('Berapa banyak angka yang ingin dimasukkan? : '))
    for x in range(n):
        num = int(input(f'Bilangan bulat ke-{x+1} : '))
        bil.append(num) 
    kuadrat(bil)
    print(f'\nBilangan               : {(bil)}\nHasil kudarat bilangan : {hasil}')
except ValueError:
    print('Input yang dimasukkan bukan berupa angka')
